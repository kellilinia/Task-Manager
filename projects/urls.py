from django.urls import path
from projects.views import list_projects, project_details




urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("projects/<int:id>/", project_details, name="show_project"),
]
