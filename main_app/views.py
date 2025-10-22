from django.shortcuts import render, redirect
from django.http import HttpResponse
#models import
from .models import Sighting, Bird
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#!auth stuff below
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


#home view 

class Home(LoginView):
    template_name = 'home.html'

#about
def about(request):
    return render (request, 'about.html')

#sightings index
def sightings_index(request):
    sightings = Sighting.objects.filter(user=request.user)
    return render(request, 'cygnus/index.html', {'sightings': sightings})

#sighting detail?
def sighting_detail(request, sighting_id):
    sighting = Sighting.objects.get(id=sighting_id)
    return render(request, 'cygnus/sight-detail.html', {'sighting': sighting})#!this should show index of birds?

#sighting create
class SightingCreate(CreateView):
    model = Sighting
    fields = ['location', 'date', 'notes']
    template_name = 'cygnus/sighting_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
