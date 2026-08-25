from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/gallery/add/', views.add_gallery_project, name='add_gallery_project'),
    path('dashboard/message/<int:pk>/', views.message_detail, name='message_detail'), # <-- Add this route
    path('dashboard/gallery/delete/<int:pk>/', views.delete_gallery_project, name='delete_gallery_project'), # <-- Add this line

]