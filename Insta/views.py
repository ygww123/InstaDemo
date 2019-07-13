from django.views.generic import TemplateView

# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'home.html'

# def get_template_names(self):
#     if self.template_name is None:
#         raise ImproperlyConfigured()

