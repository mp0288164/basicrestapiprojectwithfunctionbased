from django.urls import path 
from . import views
urlpatterns=[
    path('entry/',views.MyApiView.as_view(),name='entry'),
    path('entry/<int:id>/',views.MyApiView.as_view(),name='seen'),
]