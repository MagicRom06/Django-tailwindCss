from django.urls import path, include
from .views import NavbarPageView, TitleNavBar, TablePageView


urlpatterns = [
    path('navbar/', NavbarPageView.as_view(), name="navbar"),
    path('title/', TitleNavBar.as_view(), name="title"),
    path('table/', TablePageView.as_view(), name="table")
]
