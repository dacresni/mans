import jinja2, os, webapp2

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template()
        self.response.out.write(template.render(template_values))
