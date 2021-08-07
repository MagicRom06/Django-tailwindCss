from django.urls import path, include
from .views import NavbarPageView, TitleNavBar


urlpatterns = [
    path('navbar/', NavbarPageView.as_view(), name="navbar"),
    path('title/', TitleNavBar.as_view(), name="title")
]
