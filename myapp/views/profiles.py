from  myapp.models import Profile
from django.shortcuts import  render , redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign_in')
def profile(request):
    user = request.user
    profile = user.profile
    description = "perfil del usaurio."
    og_title="Profile"
    og_description="algo simple para el perfil del usuario."
    og_url=request.build_absolute_uri()
    og_image="https://schedulepy.nicowooow.site/static/images/logo.svg"
    
    return render(request,'profile.html',{
        "user":user,
        "profile":profile,
        "og_title":og_title,
        "description":description,
        "og_description":og_description,
        "og_url":og_url,
        "og_image":og_image,
        
    })