from django.shortcuts import render
from .models import GalleryImage


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
    return render(
        request,
        "contact.html"
    )