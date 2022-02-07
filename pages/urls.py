from django.urls import path

from .views import HomePageView, AboutPageView,TestPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('test/', TestPageView.as_view(), name='test'),
]
