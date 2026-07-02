from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home,name='home_page'),
    path('todo/<int:id>/',views.display_todo_by_id,name='display_todo_by_id'),
    path('toggle/<int:id>/',views.toggle_status,name='toggle'),
    path('todo/delete/<int:id>/',views.delete_todo_by_id,name='delete_todo'),
    path('todo/update/<int:id>/',views.update_todo_by_id,name="update_todo")
]