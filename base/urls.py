from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (CustomLoginView, DeleteView, Logout, RegisterPage,
                    TaskCreate, TaskDetail, TaskList, TaskReorder, TaskUpdate,
                    UpdateOrInsertPropertyView)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('logout/', Logout, name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

    path('update-info/', UpdateOrInsertPropertyView.as_view(), name='update_info'),
]