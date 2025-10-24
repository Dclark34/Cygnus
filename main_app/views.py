from django.shortcuts import render, redirect
from django.http import HttpResponse
#models import
from .models import Sighting, Bird, SightingBird
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import SightingForm, AddBirdToSightingForm
from django.http import Http404
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
    sighting = Sighting.objects.filter(id=sighting_id).first()
    if not sighting: 
        return Http404("404 - Sighting not found") #django version of try catch block when seing if object exists.
    
    birds_seen = SightingBird.objects.filter(sighting=sighting)

    if request.method == 'POST':
        form = AddBirdToSightingForm(request.POST)
        if form.is_valid():
            sighting_bird = form.save(commit=False)
            sighting_bird.sighting = sighting
            sighting_bird.save()
            return redirect('sight-detail', sighting_id=sighting.id)
    else:
        form = AddBirdToSightingForm()

    return render(request, 'cygnus/sightdetails.html', {
        'sighting': sighting,
        'birds_seen': birds_seen,
        'form': form,
        })

#sighting create
class SightingCreate(LoginRequiredMixin, CreateView):
    model = Sighting
    form_class = SightingForm
    template_name = 'cygnus/sighting_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
#sighting update
class SightingUpdate(LoginRequiredMixin, UpdateView):
    model = Sighting
    fields = ['location', 'notes', 'date']
    template_name = 'cygnus/sighting_form.html'


#sighting delete
class SightingDelete(LoginRequiredMixin, DeleteView):
    model = Sighting
    template_name = 'cygnus/sight_confirm_delete.html'
    success_url = '/sightings/'


#bird create
class BirdCreate(LoginRequiredMixin, CreateView):
    model = Bird
    fields = '__all__'
    template_name = 'cygnus/bird_form.html'

#bird details
class BirdDetail(LoginRequiredMixin, DetailView):
    model = Bird 
    fields = '__all__'
    template_name = 'cygnus/bird_details.html'

#bird List
class BirdList(LoginRequiredMixin, ListView):
    model = Bird
    template_name = 'cygnus/bird-index.html'

#bird update
class BirdUpdate(LoginRequiredMixin, UpdateView):
    model = Bird
    fields = '__all__'
    template_name = 'cygnus/bird_form.html'

#bird delete
class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    template_name = 'cygnus/confirm_bird_delete.html'
    success_url = '/birds/'

#associate bird with sighting
@login_required
def associate_bird(request, sighting_id, bird_id):
    Sighting.objects.get(id=sighting_id).birds.add(bird_id)
    return redirect('sight-detail', sighting_id=sighting_id)


#remove bird with sighting
@login_required
def remove_bird(request, sighting_id, bird_id):
    sighting =Sighting.objects.get(id=sighting_id)
    Sighting.birds.remove(bird_id)
    return redirect('sight-detail', sighting_id=sighting_id)

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
