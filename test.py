from src.python.report_generator.generator import ReportGenerator
from src.python.report_generator.templates import ReportTemplate
from datetime import datetime

# Create a template
template = ReportTemplate("default_template")
# Use the correct path to the template file
template.load_template("templates/default_template.txt")

# Prepare your data
data = {
    "title": "My Report", 
    "content": "This is a test report",
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Create and run the generator
generator = ReportGenerator(template, data)
report_content = generator.generate_report()

# Save the report (this would create the output directory)
generator.save_report(report_content, "output/my_report.txt")