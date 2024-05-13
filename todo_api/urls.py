from django.urls import path

from .views import TaskListApiView

urlpatterns = [
    path('api', TaskListApiView.as_view()),
]