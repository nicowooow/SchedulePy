from django import forms

from  myapp.models import Profile,Task


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