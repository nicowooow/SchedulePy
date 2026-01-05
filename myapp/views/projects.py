from django.shortcuts import  render , redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model

from myapp.models import Profile,Project,Task
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
        projects = Project.objects.filter(profile=profile)
    else:
        projects = Project.objects.none()

    print(projects)
    return render(request,'projects/projects.html',{
        "page_css": ["css/schedule-projects-tasks.css", "css/forms.css", "css/schedule.css"],
        "projects":projects,
        })
    
@login_required(login_url='sign_in')
def create_projects(request):
    print('METHOD =>', request.method)
    print('PATH   =>', request.path)
    print('POST   =>', request.POST)
    
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        done = False
        profile = request.user.profile
        Project.objects.create(title =title,description =description,done =done,date =date,profile =profile)
        return redirect('project')  
    return render(request,'projects/create_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css", "css/schedule.css"],
            "form":CreateNewProject()
            })
        
@login_required(login_url='sign_in')
def delete_projects(request):
    if request.method == 'POST':
        project_id = request.POST['project']
        project = get_object_or_404(
            Project,
            id=project_id,
            profile=request.user.profile
        )
        project.delete()
        
    return render(request,'projects/delete_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css","css/schedule.css"],
            "form":DeleteProject(user = request.user)
            })
        
@login_required(login_url='sign_in')
def update_projects(request):
    if request.method == 'POST':
        
        project = get_object_or_404(
        Project,
        id=request.POST['project'],
        profile=request.user.profile,
            )
        project.title = request.POST['title']
        project.description = request.POST['description']
        project.date = request.POST['date']  # si es DateField, mejor validarlo con un form
        project.save()
        return redirect('project')
        
    
    return render(request,'projects/update_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css","css/schedule.css"],
            "form":UpdateProject(user=request.user)
            })