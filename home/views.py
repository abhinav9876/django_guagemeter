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
class login_controller:
    #index open a login form for user
    def index(request):
        #comments = Comment.objects.order_by('-date_added')
        form = loginForm()
        #return HttpResponse("hello")
        return render(request,"login/index.html" , {'form':form})

    #loginpost get 'email id' and 'password' from user and first verify and then redirect to home page
    def loginpost(request):

        if request.method == 'POST':
            form = loginForm(request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user1, loggedIn = user.isLoggedIn(email, password)
                #isLogged is user defined function to check user in db
                if loggedIn:
                    object_list = Datatable.objects.all() #or any kind of queryset
                    print(object_list)
                    return render(request,"login/home.html",
                        {'user1':user1,'object_list':object_list,'server_url':'server_ajax'})
                else:
                    form = loginForm()
                    return render(request,"login/index.html" , {'form':form})

    #speedometer logic
    def speedometer(request):
        return render(request,"login/speedometer.html")


    #whenever you click on 'download app' button in home page it redirect here
    def app(request):
        response = HttpResponse(content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=download.zip'
        return response


    # add_test_entry add new server in db and show in datatable
    def add_test_entry(request, pk):
        if request.method == 'GET':
            test_data_list = pk.split(";")
            if Datatable.check_entry(test_data_list[0]) == "":
                Datatable.add_entry(test_data_list)
            else:
                print("already present")
        return render(request, "download/download.txt")
