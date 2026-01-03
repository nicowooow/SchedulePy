from django.shortcuts import  render

def index(request):
    user = request.user
    print(user)
    if(user.is_authenticated):
        return render(request,'home.html',{
        'page_css':["css/pages.css"],
        'user':user
        })
    
    return render(request,"index.html",{
        'page_css':"css/index.css"
    })

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
