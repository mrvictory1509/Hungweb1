from django.shortcuts import render, redirect
from home.models import User
from django.contrib.auth import authenticate
from django.db import connection
from django.contrib.auth import login as auth_user

def login(request):
    return render(request, 'login.html')
def login_user(request):
    if request.method == 'POST':
        userName = request.POST.get('userName','')
        passWord = request.POST.get('passWord','')
        # user = authenticate(username=userName, password=passWord)
        if(userName is not None):
            userID =  User.objects.filter(username = userName)[0].id
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT auth_user.username FROM auth_user WHERE id = '%s'" ,
                    [userID]
                )
                UserName = cursor.fetchall()[0][0]
            request.session.set_expiry(86400)
            if(userName == UserName):
                return redirect('/index')        
        else:
            error = {'error': 'Username already exists, please try a different username'}
            return render(request, 'login.html', error)
    else:
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')