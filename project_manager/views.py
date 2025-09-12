from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

# Create your views here.
def home(request):
    project = request.GET.get('project')
    projects = Project.objects.filter(owner=request.user) if request.user.is_authenticated else []
    return render(request, "home.html", {"project": project, "projects": projects})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})