from django.shortcuts import  render
from myapp.models import *

def index(request):
    user = request.user
    print(user)
    if(user.is_authenticated):
        return render(request,'home.html',{
        'page_css':["css/home.css"],
        'user':user
        })
    
    return render(request,"index.html",{
        'page_css':"css/index.css"
    })

def home(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()

    projects_count = Project.objects.filter(profile=profile).count() if profile else 0
    tasks_count = Task.objects.filter(project__profile=profile).count() if profile else 0
    pending_tasks = Task.objects.filter(project__profile=profile, done=False)[:5] if profile else []
    last_project = Project.objects.filter(profile=profile).order_by("-created_at").first() if profile else None

    return render(request, "home.html", {
        "page_css": ["css/home.css"],
        "user": user,
        "projects_count": projects_count,
        "tasks_count": tasks_count,
        "pending_tasks": pending_tasks,
        "last_project": last_project,
    })

def about(request):
    return render(request,'about.html',{
        "page_css":["css/home.css","css/about.css"]
    })

def calendar(request):
    return render(request,'calendar.html',{
        "page_css":["css/home.css","css/calendar.css"]
    })
