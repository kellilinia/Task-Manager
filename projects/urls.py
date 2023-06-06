from django.urls import path
from projects.views import list_projects, project_details, create_project




urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("projects/<int:id>/", project_details, name="show_project"),
    path("create/", create_project, name="create_project"),
]
