from django.shortcuts import render
from testapp.models import BangloreJobs
from  django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def Loginpage_views(request):
    if request.method=="get":
        form=AuthenticationForm(request.get)
        if form.is_valid():
            form.save()
    else:
        form=AuthenticationForm()
    return render(request,"testapp/Loginpage.html",{'form':form})

def index(request):
    return render(request,'testapp/index.html')

def BangloreJobs_views(request):
    jobs_list=BangloreJobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/BangaloreJobs.html',context=my_dict)

def HydrabadJobs_views(request):
    return render(request,"testapp/HydrabadJobs.html")

def ChennaiJobs_views(request):
    return render(request,"testapp/HydrabadJobs.html")

def PuneJobs_views(request):
    return render(request,"testapp/HydrabadJobs.html")