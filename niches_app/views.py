from django.shortcuts import render, redirect
from django.contrib import messages
from .models import GalleryImage, ContactMessage
from django.contrib.auth.decorators import login_required, user_passes_test

# Helper function to restrict access to staff/admin users only
def is_admin_user(user):
    return user.is_authenticated and user.is_staff

def home(request):
    featured_images = GalleryImage.objects.filter(
        published=True,
        featured=True
    )[:6]

    return render(
        request,
        "index.html",
        {
            "featured_images": featured_images
        }
    )

def gallery(request):
    images = GalleryImage.objects.filter(
        published=True
    )

    category = request.GET.get("category")

    if category:
        images = images.filter(
            category=category
        )

    return render(
        request,
        "gallery.html",
        {
            "images": images
        }
    )

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            service=request.POST.get("service"),
            message=request.POST.get("message"),
        )

        messages.success(
            request,
            "Thank you! Your message has been sent successfully. We will get back to you soon."
        )

        return redirect("contact")

    return render(
        request,
        "contact.html"
    )

@user_passes_test(is_admin_user, login_url='/admin/login/')
def dashboard_home(request):
    # Retrieve metrics and statistics using GalleryImage
    total_projects = GalleryImage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    
    # Retrieve recent messages and all gallery projects for display
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    all_projects = GalleryImage.objects.all()  # <-- Added this line

    context = {
        'total_projects': total_projects,
        'unread_messages': unread_messages,
        'recent_messages': recent_messages,
        'all_projects': all_projects,  # <-- Added this line to pass projects to the template
    }
    return render(request, 'dashboard/dashboard.html', context)

@user_passes_test(is_admin_user, login_url='/admin/login/')
def add_gallery_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Grab the uploaded file

        if title and image:
            GalleryImage.objects.create(
                title=title,
                description=description,
                image=image,
                published=True # Automatically publish when uploaded via dashboard
            )
            return redirect('dashboard_home') # Redirect back to overview after success

    return render(request, 'dashboard/gallery_form.html')

@user_passes_test(is_admin_user, login_url='/admin/login/')
def message_detail(request, pk):
    # Fetch the specific message or return a 404 error if it doesn't exist
    message = ContactMessage.objects.get(pk=pk)
    
    # Automatically mark the message as read when opened
    if not message.is_read:
        message.is_read = True
        message.save()

    return render(request, 'dashboard/message_detail.html', {'message': message})

@user_passes_test(is_admin_user, login_url='/admin/login/')
def delete_gallery_project(request, pk):
    # Fetch the image project or 404
    project = GalleryImage.objects.get(pk=pk)
    
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Gallery project deleted successfully.")
        return redirect('dashboard_home')
        
    return render(request, 'dashboard/delete_confirm.html', {'project': project})