# from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Profile,Project,Task 
from .forms import CreateNewProject,DeleteProject,UpdateProject
from django.shortcuts import  render , redirect
#importamos HttpResponse para poder devolver una respuesta simple

#si quieres meter numeros en la url usa <int:nombre_variable>
#si quieres meter slugs usa <slug:nombre_variable>
#si quieres meter cualquier cosa usa <path:nombre_variable>
#por defecto es str
# y para usar la variable en la vista solo tienes que llamarla por su nombre, pero antes con un comodin
# en este caso usamos %s para string
# para numeros usa %d
# luego al final del string pones % y entre parentesis la variable o variables que quieres usar
    
# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    username = "Guest"
    return HttpResponse("<h1>Welcome %s to the Home Page!</h1>" % username)

def about(request):
    return render(request,'about.html')

def calendar(request):
    return render(request,'calendar.html')

def profile(request):
    profiles = list(Profile.objects.all().values())
    profiles = list(Profile.objects.all().values())
    # return JsonResponse(profiles,safe=False)
    username = profiles[0]['username'] if profiles else 'Guest'
    return render(request,'profile.html',{
        'username':username
    })

def schedule(request):
    projects = list(Project.objects.all().values())
    tasks = list(Task.objects.all().values())
    return render(request,'schedule.html',{
        "page_css":"css/schedule-projects-tasks.css",
        "projects":projects,
        "tasks":tasks
        })
    # return JsonResponse({"projects":projects,"tasks":tasks}, safe=False)
    
def projects(request):
    return render(request,'projects/projects.html',{
        "page_css":["css/schedule-projects-tasks.css"]
        })
        
def create_projects(request):
    if request.method == 'GET':
        return render(request,'projects/create_project.html',{
            "page_css":["css/schedule-projects-tasks.css"],
            "form":CreateNewProject()
            })
    else :
        print(request.POST['title'])
        print(request.POST['description'])
        
def create_projects(request):
    if request.method == 'GET':
        return render(request,'projects/create_project.html',{
            "page_css":["css/schedule-projects-tasks.css"],
            "form":DeleteProject()
            })
    else :
        print(request.POST['title'])
        print(request.POST['description'])
        
def delete_projects(request):
    if request.method == 'GET':
        return render(request,'projects/delete_project.html',{
            "page_css":["css/schedule-projects-tasks.css"],
            "form":UpdateProject()
            })
    else :
        print(request.POST['title'])
        print(request.POST['description'])
        
def update_projects(request):
    if request.method == 'GET':
        return render(request,'projects/update_project.html',{
            "page_css":["css/schedule-projects-tasks.css"],
            "form":UpdateProject()
            })
    else :
        print(request.POST['title'])
        print(request.POST['description'])
        
    

def tasks(request):
    return render(request,'tasks/tasks.html',{
        "page_css":["css/schedule-projects-tasks.css"]
        })
    

def create_tasks(request):
    return render(request,'tasks/create_task.html',{
        "page_css":["css/schedule-projects-tasks.css"]
        })

def delete_tasks(request):
    return render(request,'tasks/delete_task.html',{
        "page_css":["css/schedule-projects-tasks.css"]
        })

def update_tasks(request):
    return render(request,'tasks/update_task.html',{
        "page_css":["css/schedule-projects-tasks.css"]
        })

def sign_in(request):
    return render(request,"signs/sign-in.html",{"page_css":"css/sign.css"})

def sign_up(request):
    return render(request,"signs/sign-up.html",{"page_css":"css/sign.css"})