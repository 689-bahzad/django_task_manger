from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    path('create/', views.add_task, name='task_create'),
    path('<int:pk>/delete/', views.delete_task, name='task_delete'),
    path('<int:pk>/finish/', views.finish_task, name='task_finish'),
]