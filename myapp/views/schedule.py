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
        projects = list(Project.objects.filter(profile=profile).values())
        tasks = list(Task.objects.filter(project__profile=profile).values())
    else:
        projects = []
        tasks = []
    return render(request,'schedule.html',{
        "page_css":"css/schedule-projects-tasks.css",
        "projects":projects,
        "tasks":tasks
        })
    # return JsonResponse({"projects":projects,"tasks":tasks}, safe=False)
    