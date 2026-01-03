from django.shortcuts import  render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from myapp.models import *
from myapp.forms import CreateNewTask,UpdateTask,DeleteTask

def tasks(request):
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
        tasks_qs = Task.objects.filter(project__profile=profile).values()
        tasks_list = list(tasks_qs)
    else:
        projects = []
        tasks_list = []
    # print("----------------------------")
    # print(projects)
    # print("----------------------------")
    # print(tasks_list)
    # print("----------------------------")
    return render(request, 'tasks/tasks.html', {
        "page_css": ["css/schedule-projects-tasks.css"],
        "projects": projects,
        "tasks": tasks_list,
    })
    

@login_required(login_url='sign_in')
def create_tasks(request):
    if request.method == 'GET':
        return render(request,'tasks/create_task.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":CreateNewTask()
            }
                  )

@login_required(login_url='sign_in')
def delete_tasks(request):
    if request.method == 'GET':
        form = DeleteTask(user=request.user)
    else :
        form = DeleteTask(request.POST, user=request.user)
    return render(request,'tasks/delete_task.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form": form
            }
                  )

@login_required(login_url='sign_in')
def update_tasks(request):
    if request.method == 'GET':
        form = UpdateTask(user=request.user)
    else :
        form = UpdateTask(request.POST, user=request.user) 
    return render(request,'tasks/update_task.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":form
            }
                    )
@login_required(login_url='sign_in')
def toggle_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # cambiar estado de la tarea
    task.done = not task.done
    task.save()

    project = task.project  # FK

    # ¿todas las tasks de este proyecto están done=True?
    all_done = Task.objects.filter(project=project, done=False).count() == 0

    project.done = all_done
    project.save()

    return redirect('task')  # o a 'task' si prefieres
