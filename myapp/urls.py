from django.urls import path
from . import views
#al poner el . haces referencia al directorio actual
# from myapp.views import home
#traes la vista home desde myapp.views
# usamos el urlpatterns para definir las rutas fuera del archivo urls de la aplicacion principal
urlpatterns = [
    path('',views.index, name="index"),
    path('home/',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('calendar/',views.calendar, name="calendar"),
    path('schedule/',views.schedule, name="schedule"),
    path('schedule/projects/',views.projects, name="project"),
    path('schedule/projects/create/',views.create_projects, name="create_project"),
    path('schedule/projects/delete/',views.delete_projects, name="delete_project"),
    path('schedule/projects/update/',views.update_projects, name="update_project"),
    path('schedule/projects/tasks/',views.tasks, name="task"),
    path('schedule/projects/tasks/create/',views.create_tasks, name="create_task"),
    path('schedule/projects/tasks/delete/',views.delete_tasks, name="delete_task"),
    path('schedule/projects/tasks/update/',views.update_tasks, name="update_task"),
    path('schedule/tasks/<int:task_id>/toggle/',views.toggle_task_done,name='toggle_task_done'),
    path('robots.txt',views.robots_txt, name="robots"),
    path('simple_sitemap.xml',views.simple_sitemap, name="simple_sitemap"),
    path('sign-in/',views.sign_in, name="sign_in"),
    path('sign-up/',views.sign_up, name="sign_up"),
    path('out-log/',views.log_out, name="log_out"),
]

    # path('profile/',views.profile, name="profile"),