from django.shortcuts import  render
from  myapp.models import Profile,Project,Task

def schedule(request):
    description = ""
    og_title="Calendar"
    og_description=""
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"
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
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
        
    })