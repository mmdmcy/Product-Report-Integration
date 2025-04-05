class ReportGenerator:
    def __init__(self, template, data):
        self.template = template
        self.data = data

    def generate_report(self):
        # Load the report template
        report_content = self.template.render_template(self.data)
        return report_content

    def save_report(self, report_content, file_path):
        with open(file_path, 'w') as report_file:
            report_file.write(report_content)