from django.views.generic.base import TemplateView

# Create your views here.
class NavbarPageView(TemplateView):
	template_name = "navbar.html"


class TitleNavBar(TemplateView):
	template_name = "title.html"
