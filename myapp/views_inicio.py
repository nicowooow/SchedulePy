# from django.shortcuts import render
from .models import Profile,Project,Task 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateNewProject,DeleteProject,UpdateProject,CreateNewTask,DeleteTask,UpdateTask
from django.shortcuts import  render , redirect, get_object_or_404, get_list_or_404
# from django.http import HttpResponse,JsonResponse
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
    user = request.user
    return render(request,'home.html',{
        'page_css':["css/pages.css"],
        'user':user
        }
                  )

def about(request):
    return render(request,'about.html')

def calendar(request):
    return render(request,'calendar.html')

@login_required(login_url='sign_in')
def profile(request):
    profiles = list(Profile.objects.all().values())
    profiles = list(Profile.objects.all().values())
    # return JsonResponse(profiles,safe=False)
    username = ""
    #profiles[0]['username'] if profiles else 'Guest'
    return render(request,'profile.html',{
        'username':username
    })

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
        projects = list(Project.objects.filter(profile=profile).values())
    else:
        projects = []
    # print(projects)
    return render(request,'projects/projects.html',{
        "page_css":["css/schedule-projects-tasks.css"],
        "projects":projects,
        })
        
@login_required(login_url='sign_in')
def create_projects(request):
    if request.method == 'GET':
        return render(request,'projects/create_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":CreateNewProject()
            })
    else :
        print(request.POST['title'])
        print(request.POST['description'])
        
@login_required(login_url='sign_in')
def delete_projects(request):
    if request.method == 'GET':
        form = DeleteProject(user=request.user)
    else :
        form = DeleteProject(request.POST, user=request.user)
        print(request.POST['title'])
        print(request.POST['description'])
    return render(request,'projects/delete_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":form
            })
        
@login_required(login_url='sign_in')
def update_projects(request):
    if request.method == 'GET':
        form = UpdateProject(user=request.user)
    else :
        form = UpdateProject(request.POST, user=request.user)
        print(request.POST['title'])
        print(request.POST['description'])
        
    
    return render(request,'projects/update_project.html',{
            "page_css":["css/schedule-projects-tasks.css","css/forms.css"],
            "form":form
            })

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



def sign_in(request):
    context = {
        "page_css":"css/sign.css",
        "action": ""
        }
    if request.method == 'POST':
        username_email = request.POST['username_email']
        password = request.POST['password']
        
        user = authenticate(request, username=username_email, password=password)
        if user is None:
            try:
                u = User.objects.get(email=username_email)
                user = authenticate(request, username=u.username, password=password)
            except User.DoesNotExist:
                user = None
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context["action"] = "username / email / password is incorrect"
            
    return render(request,"signs/sign-in.html",context)

def sign_up(request):
    context = {
        "page_css":"css/sign.css",
        "action": ""
        }
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # 1. Verificar passwords
        if password != confirm_password :
            context["action"] = "Passwords are not equal"
            return render(request, "signs/sign-up.html", context)

        # 2. Username ya usado
        if User.objects.filter(username=username).exists():
            context["action"] = "Username already registered"
            return render(request, "signs/sign-up.html", context)

        # 3. Email ya usado
        if User.objects.filter(email=email).exists():
            context["action"] = "Email already registered"
            return render(request, "signs/sign-up.html", context)
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password
            )
            
        Profile.objects.get_or_create(
            bio = "Hello, im a new user",
            user = user
        )
        login(request,user)
        return redirect('home')
        
    return render(request,"signs/sign-up.html",context)

def log_out(request):
    logout(request)
    return redirect('sign_in')