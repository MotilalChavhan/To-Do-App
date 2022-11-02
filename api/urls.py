from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view()),
    path('<int:pk>/update', views.TaskUpdate.as_view()),
    path('<int:pk>/delete', views.TaskDelete.as_view())
]