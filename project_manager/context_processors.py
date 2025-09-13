from .models import Project

def projects_context(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(owner=request.user)
    else:
        projects = Project.objects.none()
    return {'projects': projects}
