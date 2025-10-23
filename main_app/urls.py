from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name="about"),
    path('sightings/', views.sightings_index, name='index'),
    path('sightings/create/', views.SightingCreate.as_view(), name='sighting-create'),
    path('sightings/<int:sighting_id>/', views.sighting_detail, name='sight-detail'),
    path('sightings/<int:pk>/update/', views.SightingUpdate.as_view(), name='sighting-update'),
    path('sightings/<int:pk>/delete/', views.SightingDelete.as_view(), name='sighting-delete'),
    path('birds/', views.BirdList.as_view(), name='bird-index'),
    path('birds/create', views.BirdCreate.as_view(), name='bird-create'),
    path('birds/<int:pk>/', views.BirdDetail.as_view(), name='bird-detail'),
    path('birds/<int:pk>/update', views.BirdUpdate.as_view(), name='bird-update'),
    path('birds/<int:pk>/delete', views.BirdDelete.as_view(), name='bird-delete'),
    path('accounts/signup/', views.signup, name='signup'),
] 