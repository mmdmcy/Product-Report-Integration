import unittest
from src.python.report_generator.generator import ReportGenerator
from src.python.report_generator.templates import ReportTemplate

class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.report_generator = ReportGenerator()
        self.template = ReportTemplate()

    def test_generate_report(self):
        data = {"title": "Monthly Sales", "content": "Sales data for the month."}
        report = self.report_generator.generate_report(data)
        self.assertIn("Monthly Sales", report)
        self.assertIn("Sales data for the month.", report)

    def test_save_report(self):
        report_content = "This is a test report."
        file_path = "test_report.txt"
        self.report_generator.save_report(report_content, file_path)
        with open(file_path, 'r') as file:
            saved_content = file.read()
        self.assertEqual(saved_content, report_content)

    def test_load_template(self):
        template_name = "default_template"
        self.template.load_template(template_name)
        self.assertIsNotNone(self.template.template_content)

    def test_render_template(self):
        self.template.template_content = "Report Title: {{ title }}\nContent: {{ content }}"
        rendered = self.template.render_template({"title": "Test Report", "content": "This is a test."})
        self.assertIn("Report Title: Test Report", rendered)
        self.assertIn("Content: This is a test.", rendered)

if __name__ == '__main__':
    unittest.main()