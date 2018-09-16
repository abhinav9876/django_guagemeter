from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import loader
from .form import loginForm
from .models import user, Datatable
from filetransfers.api import serve_file
from wsgiref.util import FileWrapper


import json

#from .forms import CommentForm

def index(request):
    #comments = Comment.objects.order_by('-date_added')
    form = loginForm()
    #return HttpResponse("hello")
    return render(request,"login/index.html" , {'form':form})

def loginpost(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user1, loggedIn = user.isLoggedIn(email, password)
            #return HttpResponse("hello[",user1)
            print(user1,loggedIn," <-Userlog messege.........")
            if loggedIn:
                object_list = Datatable.objects.all() #or any kind of queryset
                #json1 = serializers.serialize('json', object_list)
                #json1 = json.loads(json1)
                print(object_list)
                return render(request,"login/home.html",
                    {'user1':user1,'object_list':object_list,'server_url':'server_ajax'})
            else:
                form = loginForm()
                return render(request,"login/index.html" , {'form':form})

#speedometer logic
def speedometer(request):
    return render(request,"login/speedometer.html")


#download app
def app(request):
    #try:
    #    fd=open('download/download.txt','r')
    #    return HttpResponse("hello[")
    #except:
    #    print("unsucessful to open file")
    #return render(request,"download/download.txt")
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=download.zip'
    return response

def datatable_update(request):
    print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    return render(request,"download/download.txt")
