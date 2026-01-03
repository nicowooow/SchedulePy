from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import  render , redirect
from  myapp.models import Profile

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