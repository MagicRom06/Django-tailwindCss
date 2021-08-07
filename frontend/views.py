from django.views.generic.base import TemplateView

# Create your views here.
class NavbarPageView(TemplateView):
	template_name = "home.html"
