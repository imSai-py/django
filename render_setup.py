import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialApp

User = get_user_model()

def setup():
    print("--- Starting Render Auto-Setup ---")
    
    # 1. Configure the 'Site' (required for allauth)
    # Render provides RENDER_EXTERNAL_HOSTNAME e.g. "myapp.onrender.com"
    domain = os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'localhost')
    print(f"Configuring Site ID 1 for domain: {domain}")
    
    # Use update_or_create to ensure ID=1 is correct
    site, created = Site.objects.update_or_create(
        id=1, 
        defaults={
            'domain': domain, 
            'name': 'UserProfileManagement'
        }
    )
    print(f"Site configured: {site.domain}")

    # 2. Create Superuser (if not exists)
    # You can change the password later in Admin
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123' 
    
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser '{username}'...")
        User.objects.create_superuser(username, email, password)
        print("Superuser created successfully.")
    else:
        print(f"Superuser '{username}' already exists. Skipping.")

    # 3. Configure Google SocialApp Placeholder
    # This prevents crashes if the app is missing. 
    # USER MUST UPDATE THIS IN ADMIN WITH REAL KEYS.
    print("Configuring Google SocialApp placeholder...")
    app, app_created = SocialApp.objects.update_or_create(
        provider='google',
        defaults={
            'name': 'Google',
            'client_id': 'ENTER_CLIENT_ID_IN_ADMIN',
            'secret': 'ENTER_SECRET_KEY_IN_ADMIN'
        }
    )
    # Ensure it's connected to our site
    app.sites.add(site)
    print("Google SocialApp placeholder configured.")
    
    print("--- Setup Complete ---")

if __name__ == "__main__":
    try:
        setup()
    except Exception as e:
        print(f"WARNING: Setup script encountered an error: {e}")
        # We don't raise/exit 1, so the deployment continues even if this specific script hiccups.
