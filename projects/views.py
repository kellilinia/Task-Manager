from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project


# Create your views here.


@login_required
def list_projects(request):
    list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": list,
    }
    return render(request, "projects/list.html", context)


def redirect_to_list_projects(request):
    return redirect("list_projects")
