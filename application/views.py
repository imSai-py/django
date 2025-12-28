from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm, ProfileForm, LoginForm
from .models import UserProfile

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created successfully.')
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'application/register.html', {'form': form})


def home(request):
    # Fetch 5 newest members for the "Community Pulse" section
    latest_profiles = UserProfile.objects.select_related('user').order_by('-created_at')[:5]
    total_users = UserProfile.objects.count()
    return render(request, 'home.html', {
        'latest_profiles': latest_profiles,
        'total_users': total_users
    })

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'application/profile.html', {'profile': profile})

@login_required
def update_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'application/update.html', {'form': form, 'profile': profile})

