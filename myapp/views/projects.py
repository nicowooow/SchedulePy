from django.shortcuts import  render , redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model

from myapp.models import Profile,Project,Task
from myapp.forms import CreateNewProject,DeleteProject,UpdateProject

def projects(request):

    description = "Apartado donde el usuario puede ver las Proyectos que tiene."
    og_title="Projects"
    og_description="Apartado donde el usuario puede ver las Proyectos que tiene."
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
    else:
        projects = Project.objects.none()

    print(projects)
    return render(request,'projects/projects.html',{
        "page_css": ["css/schedule-projects-tasks.css", "css/forms.css", "css/schedule.css"],
        "projects":projects,
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
        })
    
@login_required(login_url='sign_in')
def create_projects(request):
    description = "Apartado donde el usuario puede crear nuevos proyecto."
    og_title="Create Project"
    og_description="Apartado donde el usuario puede crear nuevos proyecto."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"

    if request.method == "POST":
        form = CreateNewProject(request.POST)
        if form.is_valid():
            Project.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                date=form.cleaned_data["date"],
                done=False,
                profile=request.user.profile,
            )
            return redirect("project")
    else:
        form = CreateNewProject()

    return render(
        request,
        "projects/create_project.html",
        {
            "page_css": [
                "css/schedule-projects-tasks.css",
                "css/forms.css",
                "css/schedule.css",
            ],
            "form": form,
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
        },
    )
        
@login_required(login_url='sign_in')
def delete_projects(request):
    description = "Apartado donde el usuario puede eliminar los proyectos que haiga completado o no necesite."
    og_title="Delete Project"
    og_description="Apartado donde el usuario puede eliminar los proyectos que haiga completado o no necesite."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"


    if request.method == "POST":
        form = DeleteProject(request.POST, user=request.user)
        if form.is_valid():
            project = form.cleaned_data["project"]  # ModelChoiceField
            # extra seguridad: asegurar que pertenece al usuario
            project = get_object_or_404(
                Project,
                id=project.id,
                profile=request.user.profile,
            )
            project.delete()
            return redirect("project")
    else:
        form = DeleteProject(user=request.user)

    return render(
        request,
        "projects/delete_project.html",
        {
            "page_css": [
                "css/schedule-projects-tasks.css",
                "css/forms.css",
                "css/schedule.css",
            ],
            "form": form,
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
        },
    )
     
@login_required(login_url='sign_in')
def update_projects(request):
    description = "Apartado donde el usuario puede actualizar el contenido de una proyecto seleccionada."
    og_title="Update Project"
    og_description="Apartado donde el usuario puede actualizar el contenido de una proyecto seleccionada."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"


    if request.method == "POST":
        form = UpdateProject(request.POST, user=request.user)
        if form.is_valid():
            project = form.cleaned_data["project"]
            project = get_object_or_404(
                Project,
                id=project.id,
                profile=request.user.profile,
            )
            # patch: solo cambio si el campo no viene vacío
            title = form.cleaned_data.get("title")
            if title:
                project.title = title

            description = form.cleaned_data.get("description")
            if description:
                project.description = description

            date = form.cleaned_data.get("date")
            if date is not None:
                project.date = date
            project.save()

            return redirect("project")
    else:
        form = UpdateProject(user=request.user)

    return render(
        request,
        "projects/update_project.html",
        {
            "page_css": [
                "css/schedule-projects-tasks.css",
                "css/forms.css",
                "css/schedule.css",
            ],
            "form": form,
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
        },
    )
