from django.shortcuts import  render
from  myapp.models import Profile,Project,Task

def schedule(request):
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
        tasks = Task.objects.filter(project__profile=profile)
    else:
        projects = Project.objects.none()
        tasks = Task.objects.none()

    return render(request, 'schedule.html', {
        "page_css": ["css/schedule.css", "css/schedule-projects-tasks.css"],
        "projects": projects,
        "tasks": tasks,
    })