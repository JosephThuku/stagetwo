from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from person import views

urlpatterns = [
    path('', views.PersonList.as_view()),
    path('person/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
