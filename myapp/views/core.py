from django.db.models import Count
from django.db.models.functions import TruncDate
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, redirect
from myapp.models import *

def index(request):
    description = "SchedulePy es una app web para crear proyectos, tareas y calendarios, y tener tus actividades organizadas en un solo lugar."
    og_title="SchedulePy"
    og_description="Crea proyectos, tareas y calendarios en SchedulePy y mantén tus actividades al día."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"
    user = request.user
    if(user.is_authenticated):
        return redirect("home")
    
    return render(request,"index.html",{
        'page_css':"css/index.css",
        'user':user,
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
    })

@login_required(login_url='sign_in')
def home(request):
        
    description = "Home, es donde puder visuializar ciertas opciones basicas y usarlas como atajos"
    og_title="Home - SchedulePy"
    og_description="Visualiza distintas opciones a realizar en SchedulePY."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"
    
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
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
    })

def about(request):
    description = "Una resumen del porque se creo la pagina web, y formas de contacto."
    og_title="About me"
    og_description="Hay un pequeño resumen del porque se creo la web, y de paso unos enlaces de contacto."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"
    return render(request,'about.html',{
        "page_css":["css/home.css","css/about.css"],
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
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
    
    description = "Calendario del usuario, el cual muestra cuantas tareas tiene cierto dia del mes."
    og_title="Calendar"
    og_description="Calendario del usuario, el cual muestra cuantas tareas tiene cierto dia del mes."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"
    
    return render(
        request,
        "calendar.html",
        {
            "page_css": [ "css/calendar.css","css/home.css"],
            "tasks_per_day": tasks_per_day,
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
        },
    )
