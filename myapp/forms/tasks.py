from django import forms

from  myapp.models import Project,Profile,Task


class CreateNewTask(forms.Form):
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
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    
class UpdateTask(forms.Form):
    task = forms.ModelChoiceField(
        label="Task",
        queryset=Task.objects.none()
    )
    title = forms.CharField(max_length=200, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    STATUS_CHOICES = (
        ("TODO", "TODO"),
        ("IN_PROGRESS", "IN PROGRESS"),
        ("COMPLETED", "COMPLETED"),
    )

    status = forms.ChoiceField(
        label="Status",
        choices=STATUS_CHOICES,
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