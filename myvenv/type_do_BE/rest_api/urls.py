from rest_api import views
from django.urls import path

name = 'rest_api'
urlpatterns = [
    path('todo/', views.todo),
    path('todo/<int:pk>/', views.todo_id),
    path('inprogress/', views.inprogress),
    path('inprogress/<int:pk>/', views.inprogress_id),
    path('done/', views.done),
    path('done/<int:pk>/', views.done_id),
]