from django import forms
from .models import Project,Task,Profile

class CreateNewProject(forms.Form):
    title = forms.CharField(label='New Project',max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    
class DeleteProject(forms.Form):
    project = forms.ModelChoiceField(
        label="Project",
        queryset=Project.objects.none()  # se rellena en __init__
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        qs = Project.objects.none()
        if user is not None and user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
                qs = Project.objects.filter(profile=profile)
            except Profile.DoesNotExist:
                qs = Project.objects.none()

        self.fields["project"].queryset = qs
    
class UpdateProject(forms.Form):
    project = forms.ModelChoiceField(
        label="Project",
        queryset=Project.objects.none()
    )
    title = forms.CharField(label='Name Project', max_length=200)
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        qs = Project.objects.none()
        if user is not None and user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
                qs = Project.objects.filter(profile=profile)
            except Profile.DoesNotExist:
                qs = Project.objects.none()

        self.fields["project"].queryset = qs
    
class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    
class UpdateTask(forms.Form):
    task = forms.ModelChoiceField(
        label="Task",
        queryset=Task.objects.none()
    )
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        qs = Task.objects.none()
        if user is not None and user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
                qs = Task.objects.filter(project__profile=profile)
            except Profile.DoesNotExist:
                qs = Task.objects.none()

        self.fields["task"].queryset = qs
        
class DeleteTask(forms.Form):
    task = forms.ModelChoiceField(
        label="Task",
        queryset=Task.objects.none()
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        qs = Task.objects.none()
        if user is not None and user.is_authenticated:
            try:
                profile = Profile.objects.get(user=user)
                qs = Task.objects.filter(project__profile=profile)
            except Profile.DoesNotExist:
                qs = Task.objects.none()

        self.fields["task"].queryset = qs