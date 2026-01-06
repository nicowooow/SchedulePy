from  myapp.models import Profile
from django.shortcuts import  render , redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='sign_in')
def profile(request):
    user = request.user
    profile = user.profile
    return render(request,'profile.html',{
        "user":user,
        "profile":profile
        
    })