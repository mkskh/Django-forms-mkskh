"""ToDo URL Configuration."""
from django.urls import path

from todo.views import detail_view

app_name = "todo"
urlpatterns = [
    path('<int:todo_id>/', detail_view, name="detail_view"),
]
