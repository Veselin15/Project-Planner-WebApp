from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, PlanForm, PlanContentForm
from .models import Project, Plan
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def home(request):
    """
    Home page: list all projects owned by the current user.
    If the user has exactly one project, redirect directly to it.
    """
    projects_qs = request.user.projects.order_by('-updated_at', '-created_at')
    count = projects_qs.count()
    if count == 1:
        return redirect(projects_qs.first().get_absolute_url())
    return render(request, 'home.html', {'projects': projects_qs})
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm()
    return render(request, 'project_manager/create_project.html', {'form': form})

def project_detail(request, project_id):
    """
    Project detail page:
    - Displays all plans for the project
    - Allows creating a new plan (name only)
    """
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        plan_form = PlanForm(request.POST)
        if plan_form.is_valid():
            plan = plan_form.save(commit=False)
            plan.project = project
            plan.save()
            return redirect('plan_detail', project_id=project.id, plan_id=plan.id)
    else:
        plan_form = PlanForm()

    plans = project.plans.all().order_by('created_at')
    return render(request, 'project_manager/project_detail.html', {
        'project': project,
        'plans': plans,
        'plan_form': plan_form,
    })

def plan_detail(request, project_id, plan_id):
    """
    Plan detail/edit page:
    - Displays CKEditor for plan.content and allows editing plan name and content.
    """
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    plan = get_object_or_404(Plan, id=plan_id, project=project)

    if request.method == 'POST':
        form = PlanContentForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plan_detail', project_id=project.id, plan_id=plan.id)
    else:
        form = PlanContentForm(instance=plan)

    plans = project.plans.all().order_by('created_at')
    return render(request, 'project_manager/plan_detail.html', {
        'project': project,
        'plan': plan,
        'plans': plans,
        'form': form,
    })