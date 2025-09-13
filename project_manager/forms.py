from django import forms
from ckeditor.widgets import CKEditorWidget
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
    """
    Form used on the plan detail page to edit a plan's name and rich text content.
    Uses Django CKEditor widget for the content field.
    """
    class Meta:
        model = Plan
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plan name'}),
            'content': CKEditorWidget(),
        }