import json
import os
import datetime

# Create directories for dashboard
os.makedirs('output/dashboard', exist_ok=True)

# Load the security data
with open('output/transformed_security_data.json', 'r') as f:
    security_data = json.load(f)

# Sort data by status (Critical first, then Warning, then Good)
def status_priority(item):
    if item['status'] == 'Critical':
        return 0
    elif item['status'] == 'Warning':
        return 1
    else:
        return 2

security_data.sort(key=status_priority)

# Get the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create an HTML dashboard - using triple double quotes to avoid formatting issues
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Status Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .dashboard {{
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            text-align: center;
        }}
        .summary {{
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
            text-align: center;
        }}
        .summary-item {{
            padding: 15px;
            border-radius: 5px;
            width: 30%;
        }}
        .critical {{
            background-color: #ffdddd;
            color: #d8000c;
            border-left: 6px solid #d8000c;
        }}
        .warning {{
            background-color: #feefb3;
            color: #9f6000;
            border-left: 6px solid #9f6000;
        }}
        .good {{
            background-color: #dff2bf;
            color: #4f8a10;
            border-left: 6px solid #4f8a10;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        .progress-bar {{
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
        }}
        .progress {{
            height: 100%;
            text-align: center;
            color: white;
            font-weight: bold;
        }}
        .status-critical {{
            background-color: #d8000c;
        }}
        .status-warning {{
            background-color: #9f6000;
        }}
        .status-good {{
            background-color: #4f8a10;
        }}
        .attention {{
            font-weight: bold;
            color: #d8000c;
        }}
        .date {{
            text-align: right;
            color: #666;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="dashboard">
        <h1>Security Status Dashboard</h1>
        <p class="date">Generated on: {current_date}</p>
        
        <div class="summary">
"""

# Count status occurrences
status_counts = {'Critical': 0, 'Warning': 0, 'Good': 0}
for item in security_data:
    status_counts[item['status']] += 1

# Add summary boxes
html_content += f"""
            <div class="summary-item critical">
                <h2>{status_counts['Critical']}</h2>
                <p>Critical Issues</p>
            </div>
            <div class="summary-item warning">
                <h2>{status_counts['Warning']}</h2>
                <p>Warning Issues</p>
            </div>
            <div class="summary-item good">
                <h2>{status_counts['Good']}</h2>
                <p>Good Status</p>
            </div>
        </div>
"""

# Add table with items
html_content += """
        <h2>Security Items Detail</h2>
        <table>
            <tr>
                <th>Item Name</th>
                <th>Value</th>
                <th>Status</th>
                <th>Progress</th>
                <th>Action Required</th>
            </tr>
"""

# Add rows for each item
for item in security_data:
    status_class = f"status-{item['status'].lower()}"
    progress_width = f"{item['value']}%"
    
    action_required = "IMMEDIATE ACTION REQUIRED" if item['status'] == 'Critical' else \
                      "Monitor and improve" if item['status'] == 'Warning' else \
                      "No action needed"
    
    action_class = "attention" if item['status'] == 'Critical' else ""
    
    html_content += f"""
            <tr>
                <td>{item['metric_name']}</td>
                <td>{item['formatted_value']}</td>
                <td>{item['status']}</td>
                <td>
                    <div class="progress-bar">
                        <div class="progress {status_class}" style="width: {progress_width}">{item['formatted_value']}</div>
                    </div>
                </td>
                <td class="{action_class}">{action_required}</td>
            </tr>
    """

# Close the HTML tags
html_content += """
        </table>
    </div>
</body>
</html>
"""

# Write the HTML file
with open('output/dashboard/security_dashboard.html', 'w') as f:
    f.write(html_content)

print("Dashboard created: 'output/dashboard/security_dashboard.html'")