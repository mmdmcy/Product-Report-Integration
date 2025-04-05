from src.python.report_generator.generator import ReportGenerator
from src.python.report_generator.templates import ReportTemplate
from datetime import datetime
import os
import json
import uuid

# Create output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Create a template
template = ReportTemplate("advanced_template")
template.load_template("templates/advanced_template.txt")

# Prepare your data with more complex structure
data = {
    "title": "Q1 2025 Product Performance Report",
    "executive_summary": "This quarter showed a 15% increase in overall product performance, with notable improvements in reliability metrics.",
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "report_id": str(uuid.uuid4()),
    "author": "Automated System",
    "department": "Product Engineering",
    "metrics": [
        {"name": "Performance Index", "current_value": "98.7", "previous_value": "92.3", "change": "+6.9"},
        {"name": "Reliability Score", "current_value": "99.2%", "previous_value": "97.5%", "change": "+1.7"},
        {"name": "User Satisfaction", "current_value": "4.8/5", "previous_value": "4.6/5", "change": "+4.3"},
        {"name": "Processing Time", "current_value": "0.45s", "previous_value": "0.62s", "change": "-27.4"}
    ],
    "detailed_analysis": """
Our product performance has shown significant improvement this quarter due to the implementation of
several key optimizations:

1. Enhanced caching mechanisms reducing database load by 40%
2. Upgraded hardware infrastructure providing 30% more processing capacity
3. Code refactoring resulting in 15% reduction in execution time

These changes have contributed to the overall performance boost observed across all metrics.
""",
    "charts": [
        {"name": "Performance Trend", "description": "Shows performance evolution over the past 6 quarters"},
        {"name": "Resource Utilization", "description": "Breakdown of system resource usage by component"},
        {"name": "Error Rate Analysis", "description": "Distribution of errors by category and severity"}
    ],
    "recommendations": [
        {"title": "Further Optimize Database Queries", "description": "Implement prepared statements and query caching to improve database response times."},
        {"title": "Enhance Monitoring Systems", "description": "Deploy advanced monitoring for early detection of performance degradation."},
        {"title": "Scale Cloud Resources", "description": "Increase cloud resource allocation to accommodate growing user base."}
    ],
    "conclusion": "The system is performing exceptionally well, showing improvements across all key metrics. The implemented optimizations have had a significant positive impact, and further enhancements are planned for Q2.",
    "appendix": "Raw data and detailed test results are available in the attached spreadsheet.",
    "support_contact": "support@example.com"
}

# Create and run the generator
generator = ReportGenerator(template, data)
report_content = generator.generate_report()

# Save the report
report_filename = f"output/product_performance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
generator.save_report(report_content, report_filename)

print(f"Advanced report generated: {report_filename}")

# Also save the data as JSON for reference
with open(f"output/report_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'w') as f:
    json.dump(data, f, indent=2)