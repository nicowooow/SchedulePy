from django import forms

class CreateNewProject(forms.Form):
    title = forms.CharField(label='New Project',max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    
class DeleteProject(forms.Form):
    title = forms.CharField(label='Name Project',max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    
class UpdateProject(forms.Form):
    title = forms.CharField(label='Name Project',max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    
class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    