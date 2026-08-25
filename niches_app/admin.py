from django.contrib import admin
from .models import GalleryImage, ContactMessage



@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "published",
        "display_order",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "published",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "featured",
        "published",
        "display_order",
    )

    ordering = (
        "display_order",
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "description",
                    "category",
                )
            },
        ),
        (
            "Project Image",
            {
                "fields": (
                    "image",
                )
            },
        ),
        (
            "Website Display",
            {
                "fields": (
                    "featured",
                    "published",
                    "display_order",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )
    
    # =========================================
# CONTACT MESSAGES
# =========================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "service",
        "created_at",
    )

    list_filter = (
        "service",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "message",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "name",
        "email",
        "phone",
        "service",
        "message",
        "created_at",
    )