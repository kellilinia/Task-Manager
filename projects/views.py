from django.shortcuts import render
from projects.models import Project


# Create your views here.
def list_projects(request):
    list = Project.objects.all()
    context = {
        "project_list": list,
    }
    return render(request, "projects/list.html", context)
