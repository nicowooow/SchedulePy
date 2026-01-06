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
        "page_css":["css/schedule-projects-tasks.css","css/schedule.css","css/task.css"],
        "projects": projects,
        "tasks": tasks_list,
    })
    

@login_required(login_url='sign_in')
def create_tasks(request):
    if request.method == "POST":
        form = CreateNewTask(request.POST, user=request.user)
        if form.is_valid():
            project = get_object_or_404(
                Project,
                id=form.cleaned_data["project"].id,
                profile=request.user.profile,
            )

            Task.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                status="TODO",
                project=project,
            )
            return redirect("task")
    else:
        form = CreateNewTask(user=request.user)

    return render(
        request,
        'tasks/create_task.html',
        {
            "page_css": ["css/schedule-projects-tasks.css", "css/forms.css", "css/task.css", "css/schedule.css"],
            "form": form,
        },
    )


@login_required(login_url='sign_in')
def delete_tasks(request):
    if request.method == "POST":
        form = DeleteTask(request.POST, user=request.user)
        if form.is_valid():
            task = form.cleaned_data["task"]  # ModelChoiceField en DeleteTask
            task = get_object_or_404(
                Task,
                id=task.id,
                project__profile=request.user.profile,
            )
            task.delete()
            return redirect("task")
    else:
        form = DeleteTask(user=request.user)

    return render(
        request,
        'tasks/delete_task.html',
        {
            "page_css": ["css/schedule-projects-tasks.css", "css/forms.css", "css/task.css", "css/schedule.css"],
            "form": form,
        },
    )


@login_required(login_url='sign_in')
def update_tasks(request):
    if request.method == "POST":
        form = UpdateTask(request.POST, user=request.user)
        if form.is_valid():
            task_obj = form.cleaned_data["task"]
            task = get_object_or_404(
                Task,
                id=task_obj.id,
                project__profile=request.user.profile,
            )

            # patch: solo actualiza si viene valor
            title = form.cleaned_data.get("title")
            if title:
                task.title = title

            description = form.cleaned_data.get("description")
            if description:
                task.description = description

            status = form.cleaned_data.get("status")
            if status:
                task.status = status

            task.save()
            return redirect("task")
    else:
        form = UpdateTask(user=request.user)

    return render(
        request,
        'tasks/update_task.html',
        {
            "page_css": ["css/schedule-projects-tasks.css", "css/forms.css", "css/task.css", "css/schedule.css"],
            "form": form,
        },
    )

    
@login_required(login_url='sign_in')
def toggle_task_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # cambiar estado de la tarea
    task.done = not task.done
    task.status = "COMPLETED" if task.done else "TODO"
    task.save()

    project = task.project  # FK

    # ¿todas las tasks de este proyecto están done=True?
    all_done = Task.objects.filter(project=project, done=False).count() == 0

    project.done = all_done
    project.save()

    return redirect('task')  # o a 'task' si prefieres
