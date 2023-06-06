from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import CreateProjectForm


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


@login_required
def project_details(request, id):
    instance = Project.objects.get(id=id)
    context = {
        "project_instance": instance,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
