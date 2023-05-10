from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo


# Create your views here.
def home(request):
    ss = Todo()
    if request.method=='POST':
        if True:
            ss.Name=request.POST.get('Name')
            ss.Designation=request.POST.get('Designation')
            ss.Date_Of_Birth=request.POST.get('Date_Of_Birth')
            ss.save()
            return redirect('data/')
    return render(request,'home.html')

def data(request):
    kk=Todo.objects.all()
    return render(request,'data.html',locals())

def data_list(request,id):
    ss=Todo.objects.get(pk=id)
    return render (request,'data_list.html',{'aa':ss})
