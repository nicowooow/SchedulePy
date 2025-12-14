from myapp import views
from django.urls import path
from . import views
#al poner el . haces referencia al directorio actual
# from myapp.views import home
#traes la vista home desde myapp.views
# usamos el urlpatterns para definir las rutas fuera del archivo urls de la aplicacion principal
urlpatterns = [
    path('',views.index),
    path('home/',views.home),
    path('about/',views.about),
    path('calendar/',views.calendar),
    path('schedule/',views.schedule),
    path('schedule/projects/',views.projects),
    path('schedule/projects/create/',views.create_projects),
    path('schedule/projects/delete/',views.delete_projects),
    path('schedule/projects/update/',views.update_projects),
    path('schedule/projects/tasks/',views.tasks),
    path('schedule/projects/tasks/create/',views.create_tasks),
    path('schedule/projects/tasks/delete/',views.delete_tasks),
    path('schedule/projects/tasks/update/',views.update_tasks),
    path('profile/',views.profile),
    path('sign-in/',views.sign_in),
    path('sign-up/',views.sign_up),
]
