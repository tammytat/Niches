import os
from django.apps import AppConfig


class NichConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'niches_app'

    def ready(self):
        # Auto-create superuser on startup using environment variables
        try:
            from django.contrib.auth.models import User
            username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
            email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "admin@nichesandhues.com")
            password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "SuperSecurePassword123")

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
        except Exception:
            # Passes silently if database tables aren't migrated yet during build time
            pass