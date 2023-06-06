from django.urls import path
from tasks.views import task_instance


urlpatterns = [
    path("create/", task_instance, name="create_task"),
]
