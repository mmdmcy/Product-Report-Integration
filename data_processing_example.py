from src.python.data_processors.cleaner import DataCleaner
from src.python.data_processors.transformer import DataTransformer
from src.python.integrations.api_client import APIClient
from src.python.utils.logger import Logger
from src.python.utils.config import Config
import json
import os
import datetime
import random
import time

# Initialize components
logger = Logger('data_processing.log')
cleaner = DataCleaner()
transformer = DataTransformer()

# Create mock API client (since we don't have actual endpoints)
class MockAPIClient:
    def __init__(self):
        self.base_url = "https://mockapi.example.com"
        self.api_key = "mock_api_key_123"
    
    def fetch_data(self, endpoint):
        """Mock data fetching with realistic delays and random data"""
        logger.log_info(f"Fetching data from {endpoint}")
        time.sleep(0.5)  # Simulate network delay
        
        # Generate mock data based on endpoint
        if endpoint == "performance":
            data = [
                {"id": i, "name": f"Metric {i}", "value": str(random.uniform(80, 99.9))} 
                for i in range(1, 15)
            ]
        elif endpoint == "reliability":
            data = [
                {"id": i, "name": f"Component {i}", "value": str(random.uniform(95, 99.99))} 
                for i in range(1, 10)
            ]
        else:
            data = [
                {"id": i, "name": f"Item {i}", "value": str(random.uniform(1, 100))} 
                for i in range(1, 8)
            ]
            
        # Add some incomplete data for cleaning demo
        data.append({"id": len(data)+1, "name": None, "value": None})
        data.append({"id": None, "name": "Invalid Entry", "value": "error"})
        
        logger.log_info(f"Retrieved {len(data)} records from {endpoint}")
        return data

# Create mock API client
api_client = MockAPIClient()

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def process_data_source(source_name):
    """Process data from a specific source"""
    logger.log_info(f"Processing data source: {source_name}")
    
    # 1. Fetch raw data
    raw_data = api_client.fetch_data(source_name)
    
    # Save raw data for reference
    with open(f"output/raw_{source_name}_data.json", 'w') as f:
        json.dump(raw_data, f, indent=2)
    
    # 2. Clean the data
    logger.log_info(f"Cleaning {len(raw_data)} records from {source_name}")
    cleaned_data = []
    for item in raw_data:
        if item.get('id') is not None and item.get('name') is not None and item.get('value') is not None:
            cleaned_item = {
                'id': item['id'],
                'name': item['name'].strip(),
                'value': item['value']
            }
            cleaned_data.append(cleaned_item)
    
    logger.log_info(f"After cleaning: {len(cleaned_data)} records remain")
    
    # Save cleaned data
    with open(f"output/cleaned_{source_name}_data.json", 'w') as f:
        json.dump(cleaned_data, f, indent=2)
    
    # 3. Transform the data
    logger.log_info(f"Transforming data from {source_name}")
    transformed_data = []
    for item in cleaned_data:
        try:
            transformed_item = {
                'identifier': int(item['id']),
                'metric_name': item['name'].title(),
                'value': float(item['value']),
                'formatted_value': f"{float(item['value']):.2f}%",
                'status': 'Good' if float(item['value']) > 90 else 'Warning' if float(item['value']) > 80 else 'Critical'
            }
            transformed_data.append(transformed_item)
        except ValueError as e:
            logger.log_error(f"Transformation error for item {item}: {e}")
    
    logger.log_info(f"Transformation complete: {len(transformed_data)} records processed")
    
    # Save transformed data
    with open(f"output/transformed_{source_name}_data.json", 'w') as f:
        json.dump(transformed_data, f, indent=2)
    
    return transformed_data

# Process multiple data sources
data_sources = ["performance", "reliability", "security"]
all_processed_data = {}

for source in data_sources:
    logger.log_info(f"Starting processing workflow for {source}")
    processed_data = process_data_source(source)
    all_processed_data[source] = processed_data
    logger.log_info(f"Completed processing workflow for {source}")

# Create a consolidated data file
consolidated_data = {
    "report_metadata": {
        "generation_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_sources": data_sources,
        "record_count": sum(len(all_processed_data[source]) for source in data_sources)
    },
    "data": all_processed_data
}

with open("output/consolidated_report_data.json", 'w') as f:
    json.dump(consolidated_data, f, indent=2)

logger.log_info(f"Data processing complete. Consolidated data saved to output/consolidated_report_data.json")
print("Data processing complete. Check the output directory for results.")