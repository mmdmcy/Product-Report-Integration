import json
import csv
import os

# Create directories for exports
os.makedirs('output/exports', exist_ok=True)

# Load the security data
with open('output/transformed_security_data.json', 'r') as f:
    security_data = json.load(f)

# Export to CSV
with open('output/exports/security_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Item Name', 'Value', 'Formatted Value', 'Status', 'Needs Attention']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for item in security_data:
        # Add a column that explicitly states if attention is needed
        needs_attention = "YES - IMMEDIATE ACTION" if item['status'] == 'Critical' else \
                          "YES - Monitor" if item['status'] == 'Warning' else "No"
        
        writer.writerow({
            'Item Name': item['metric_name'],
            'Value': item['value'],
            'Formatted Value': item['formatted_value'],
            'Status': item['status'],
            'Needs Attention': needs_attention
        })

print("CSV file created: 'output/exports/security_data.csv'")