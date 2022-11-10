from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('', views.TaskList.as_view()),
    path('<int:pk>/update', views.TaskUpdate.as_view()),
    path('<int:pk>/delete', views.TaskDelete.as_view())
]