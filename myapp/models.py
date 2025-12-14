from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    done = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title+' - '+self.id_proyect.title
    
#para subir estos cambios podemos usar :
# python manage.py makemigrations myapp, para que los cambios en myapp
#python manage.py migrate, para aplicar los cambios a la base de datos

#si quieres guardar datos en la base de datos puedes usar el shell de django
# python manage.py shell
# from myapp.models import Profile, Proyect, Task
# 
# p = Profile(username='user1', bio='This is user 1', email='nico@gmail.com0', password='1234')
# p.save()
# esto crea un nuevo perfil y lo guarda en la base de datos, lo mismo con los demas modelos
# pr = p.proyect_set.create(title='Project 1', description='This is project 1', created_at='2024-06-01 10:00:00')
# t = pr.task_set.create(title='Task 1', description='This is task 1', status='Pending', due_date='2024-06-10 10:00:00')
# 
# esto crea un nuevo proyecto asociado al perfil y una tarea asociada al proyecto
#creamos un def __str__(self): en cada modelo para que al imprimir el objeto nos muestre algo mas util que <Profile object (1)>
# y retornamos el valor que buscamos mostrar, en este caso el username, title, etc.f