from django.urls import path
from django.conf.urls import include,url
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path("registered/", views.register_done, name='register_done'),
    path("terms/", views.terms, name='terms'),
    path('stimuli/',views.show_stimuli_one_by_one,name='show_stimuli_one_by_one'),
    path('instructions/',views.instructions,name='instructions'),
    path('questions/',views.save_responses, name='save_responses'),
    path('Features/',views.save_responses_features, name='save_responses_features'),
path('Description/',views.save_responses_description, name='save_responses_description'),
]

