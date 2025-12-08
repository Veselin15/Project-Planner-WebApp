from django import forms
from .models import Project, Plan

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Optional description'}),
        }

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plan name'})
        }

class PlanContentForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'content']
        # CHANGED: Use HiddenInput for content. JS will fill this.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border-0 fw-bold fs-2', 'placeholder': 'Untitled Plan'}),
            'content': forms.HiddenInput(),
        }