from django.shortcuts import render, redirect
from django.http import HttpResponse
#models import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#import forms
#!auth stuff below
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


#home view TODO: refactor to be a class based view with a login.

class Home(LoginView):
    template_name = 'home.html'

#about
def about(request):
    return render (request, 'about.html')


#sign up function
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('/')
        else:
            error_message = 'Invalid sign up - Please try again'
    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'signup.html', context)
