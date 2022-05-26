from django.urls import path
from demo import views
urlpatterns = [
    path('',views.home,name='' ),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('skill/',views.skill,name='skill'),
]
