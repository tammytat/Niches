from django.contrib import admin
from .models import GalleryImage


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