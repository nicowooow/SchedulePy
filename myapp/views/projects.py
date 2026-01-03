from django.shortcuts import  render , redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from myapp.models import Profile,Project
from myapp.forms import CreateNewProject,DeleteProject,UpdateProject

def projects(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None
    else:
        try:
            profile = Profile.objects.get(id=1)
        except Profile.DoesNotExist:
            profile = None
            
    if profile is not None:
        projects = list(Project.objects.filter(profile=profile).values())
    else:
        projects = []
    # print(projects)
    return render(request,'projects/projects.html',{
        "page_css":["css/schedule-projects-tasks.css"],
        "projects":projects,
        })
    
@login_required(login_url='sign_in')
def create_projects(request):
    if request.method == 'GET':
        return render(request,'projects/create_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":CreateNewProject()
            })
    else :
        print(request.POST['title'])
        print(request.POST['description'])
        
@login_required(login_url='sign_in')
def delete_projects(request):
    if request.method == 'GET':
        form = DeleteProject(user=request.user)
    else :
        form = DeleteProject(request.POST, user=request.user)
        print(request.POST['title'])
        print(request.POST['description'])
    return render(request,'projects/delete_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":form
            })
        
@login_required(login_url='sign_in')
def update_projects(request):
    if request.method == 'GET':
        form = UpdateProject(user=request.user)
    else :
        form = UpdateProject(request.POST, user=request.user)
        print(request.POST['title'])
        print(request.POST['description'])
        
    
    return render(request,'projects/update_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":form
            })