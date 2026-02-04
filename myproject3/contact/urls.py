from django.urls import path

from . import views

urlpatterns = [
    path('responses/', views.view_responses, name='responses'),
    path('', views.contact_page, name='contact'),
]