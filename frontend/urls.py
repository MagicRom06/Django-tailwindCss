from django.urls import path, include
from .views import NavbarPageView


urlpatterns = [
    path('', NavbarPageView.as_view(), name="home")
]
