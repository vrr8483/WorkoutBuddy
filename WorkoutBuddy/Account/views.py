from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate

def login(request):
    if request.GET.get('username') is None or request.GET.get("password") is None:
        return HttpResponse(render(request, 'energize_andover/Login.html', {'message': "Login Failed: Missing Username and/or Password"}))
    user = authenticate(username=request.GET.get('username'), password=request.GET.get('password'))
    if user is not None:
        request.session['logged_in'] = True;
        request.session['username'] = request.GET.get('username')
        request.session['password'] = request.GET.get('password')
        message = "User " + request.session['username'] + " logged in."
        return HttpResponseRedirect(request.session['destination'])
    else:
        return HttpResponse(render(request, 'energize_andover/Login.html', {'message': "Login Failed: Missing Username and/or Password"}))
