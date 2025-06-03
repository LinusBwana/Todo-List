from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path('', views.home, name = "home"),
    path('newtask/', views.new_task, name = "new_task"),
    path('displaytasks/', views.display_tasks, name = "display_tasks"),
    path('edittask/<int:task_id>/', views.edit_task, name = "edit_task"),
    path('deletetask/<int:task_id>/', views.delete_task, name = "delete_task"),
    path('confirm_delete/', views.confirm_delete, name = "confirm_delete"),
    path('login/', views.user_login, name = "user_login"),
    path('signup/', views.user_signup, name = "user_signup"),
    path('logout/', views.user_logout, name = "user_logout"),
]