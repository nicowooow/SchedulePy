from  myapp.models import Profile
from django.shortcuts import  render , redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

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