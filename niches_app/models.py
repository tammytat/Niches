from django.db import models


class GalleryImage(models.Model):

    CATEGORY_CHOICES = [
        ("residential", "Residential Interior"),
        ("commercial", "Commercial Interior"),
        ("renovation", "Renovation & Remodelling"),
        ("furniture", "Furniture Design"),
        ("decor", "Décor"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    featured = models.BooleanField(
        default=False
    )

    published = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["display_order", "-created_at"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.title
    
    
# =========================================
# CONTACT MESSAGES
# =========================================

class ContactMessage(models.Model):

    SERVICE_CHOICES = [
        ("residential", "Residential Interior Design"),
        ("commercial", "Commercial Interior Design"),
        ("renovation", "Renovation & Remodelling"),
        ("consultation", "Design Consultation"),
    ]

    name = models.CharField(
        max_length=200
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    service = models.CharField(
        max_length=30,
        choices=SERVICE_CHOICES,
        blank=True
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )  # <-- Added this field required by your dashboard

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.service}"