from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, AboutView, ContactView

app_name = 'website'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
