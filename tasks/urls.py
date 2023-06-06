from django.urls import path
from tasks.views import task_instance, task_list


urlpatterns = [
    path("create/", task_instance, name="create_task"),
    path("mine/", task_list, name="show_my_tasks"),
]
