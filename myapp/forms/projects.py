from django import forms
from myapp.models import Profile,Project

class CreateNewProject(forms.Form):
    title = forms.CharField(label='New Project',max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(
        label='Due date',
        widget=forms.DateInput(
            attrs={
                'type': 'date'  # HTML5 date picker
            }
        )
    )
    
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
    date = forms.DateField(
        label='Due date',
        widget=forms.DateInput(
            attrs={
                'type': 'date'  # HTML5 date picker
            }
        )
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