from django.db.models import Count
from django.db.models.functions import TruncDate
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='sign_in')
def home(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()

    projects_count = Project.objects.filter(profile=profile).count() if profile else 0
    tasks_count = Task.objects.filter(project__profile=profile).count() if profile else 0
    pending_tasks = Task.objects.filter(project__profile=profile, done=False)[:5] if profile else []
    last_project = Project.objects.filter(profile=profile).order_by("-created_at").first() if profile else None

    print(projects_count)
    print(tasks_count)
    print(pending_tasks)
    print(last_project)
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
    tasks_per_day=[]
    if request.user.is_authenticated and hasattr(request.user, "profile"):
        profile = request.user.profile
        tasks_per_day_qs = (
            Task.objects
            .filter(project__profile=profile)
            .annotate(day=TruncDate('due_date'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )
        # Lo convertimos a dict { "YYYY-MM-DD": cantidad }
        tasks_per_day = {
            item["day"].strftime("%Y-%m-%d"): item["count"]
            for item in tasks_per_day_qs
        }
    
    return render(
        request,
        "calendar.html",
        {
            "page_css": [ "css/calendar.css","css/home.css"],
            "tasks_per_day": tasks_per_day,
        },
    )
