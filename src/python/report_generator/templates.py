class ReportTemplate:
    def __init__(self, template_name):
        self.template_name = template_name
        self.template_content = ""

    def load_template(self, file_path):
        """Load the report template from a file."""
        try:
            with open(file_path, 'r') as file:
                self.template_content = file.read()
        except FileNotFoundError:
            print(f"Template file {file_path} not found.")
        except Exception as e:
            print(f"An error occurred while loading the template: {e}")

    def render_template(self, context):
        """Render the template with the given context."""
        rendered_content = self.template_content
        for key, value in context.items():
            rendered_content = rendered_content.replace(f"{{{{ {key} }}}}", str(value))
        return rendered_content