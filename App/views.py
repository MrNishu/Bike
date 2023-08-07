from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib .auth import authenticate, login
from .models import MyDb, Admin
from .models import models


# Create your views here.



def HomePage(request):
      return render(request, 'App/index.html')


def AboutPage(request):
      return render (request, 'App/about.html') 


def ContactPage(request):
      if request.method == 'POST':
            
            F = request.POST.get('FullNames')
            E = request.POST.get('Emails')
            Q = request.POST.get('Querries')
            g = request.POST.get('Genders')

            data = MyDb(Full_Name = F, EMail =E, Querry = Q, Gender = g)
            data.save( )
            messages.error(request,'Successfully ho gaya apna kaam yess!!')


      return render (request, 'App/contact.html')
      


def ServicesPage(request):

      return render (request, 'App/services.html')
      


def Admin(request):
      if request.method == 'POST':
         
            UserN = request.POST.get('UserName')
            UserK= request.POST.get('UserKey')
            UserP= request.POST.get('UserPassword')
            print(UserN, UserK, UserP)
      

            user = authenticate(request, AdminID = UserN, AdminKey = UserK, AdminPassword = UserP)
            if user is not None:

                  login(request, user)
                  return redirect('/')
            else:
                  messages.error(request,'Username or Password incorrect')

          
      return render (request, 'App/Admin_Login.html')

#Delete Model

      


def index(request):
      datas = MyDb.objects.all()
      messages.success(request,'Successfully ho gaya apna kaam yess!!')
      return render (request, 'App/index1.html', {'datas': datas})


#Delete Record

def delete(request,UserId):
    MyDb = models.MyDb.objects.get(id=UserId)
    MyDb.delete()
    return redirect('/')


#Update Record

def update(request,UserId):
    MyDb = models.MyDb.objects.get(id=UserId)
    if request.POST:
        MyDb.Full_Name = request.POST['FullName']
        MyDb.EMail = request.POST['Email']
        MyDb.Querry = request.POST['Querry']
        MyDb.Gender = request.POST['Gender']
        MyDb.save()
        return redirect('/')
    data = {
        'heading':'Update MyDb',
        'MyDb':'MyDb'
    }
    return render(request,'/',context=data)

