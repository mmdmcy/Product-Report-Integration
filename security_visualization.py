import json
import matplotlib.pyplot as plt
import numpy as np
import os

# Create directories for visualizations
os.makedirs('output/visualizations', exist_ok=True)

# Load the security data
with open('output/transformed_security_data.json', 'r') as f:
    security_data = json.load(f)

# Sort data by value (ascending)
security_data.sort(key=lambda x: x['value'])

# Extract data for plotting
item_names = [item['metric_name'] for item in security_data]
values = [item['value'] for item in security_data]
statuses = [item['status'] for item in security_data]

# Define colors based on status
colors = []
for status in statuses:
    if status == 'Critical':
        colors.append('red')
    elif status == 'Warning':
        colors.append('orange')
    else:
        colors.append('green')

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(item_names, values, color=colors)

# Add percentage labels to the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, 
             f'{width:.1f}%', ha='left', va='center')

# Add a vertical line for the threshold (90%)
plt.axvline(x=90, color='green', linestyle='--', alpha=0.7, label='Good Threshold (90%)')
plt.axvline(x=80, color='orange', linestyle='--', alpha=0.7, label='Warning Threshold (80%)')

# Customize the plot
plt.title('Security Items Status (Items Requiring Attention Highlighted)', fontsize=15)
plt.xlabel('Security Score (%)', fontsize=12)
plt.ylabel('Security Items', fontsize=12)
plt.xlim(0, 105)  # Set x-axis limit to accommodate labels
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Add annotation about critical items
critical_items = [item['metric_name'] for item in security_data if item['status'] == 'Critical']
critical_text = "Critical Items Requiring Immediate Attention:\n• " + "\n• ".join(critical_items)
plt.figtext(0.15, 0.01, critical_text, fontsize=12, color='red')

# Save the visualization
plt.tight_layout()
plt.savefig('output/visualizations/security_status.png', dpi=300)
plt.savefig('output/visualizations/security_status.pdf')
plt.close()

# Create a pie chart showing status distribution
status_counts = {'Critical': 0, 'Warning': 0, 'Good': 0}
for status in statuses:
    status_counts[status] += 1

labels = status_counts.keys()
sizes = status_counts.values()
colors_pie = ['red', 'orange', 'green']
explode = (0.1, 0, 0)  # explode the 1st slice (Critical)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors_pie,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title('Distribution of Security Item Status', fontsize=15)
plt.savefig('output/visualizations/security_status_pie.png', dpi=300)
plt.savefig('output/visualizations/security_status_pie.pdf')

print("Visualizations created in 'output/visualizations/' directory")