from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('event-details/<int:pk>',views.eventdetail,name='eventdetail')
]