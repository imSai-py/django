from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False, label='Bio (optional)')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'bio')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = UserProfile.objects.create(user=user, bio=self.cleaned_data['bio'])
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'photo']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', False)
        if photo:
            if photo.size > 2 * 1024 * 1024:  # 2MB limit
                raise forms.ValidationError("Photo size must be under 2MB.")
            if not photo.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise forms.ValidationError("Only PNG/JPG images allowed.")
        return photo

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username',
            'class': 'input-field',
            'id': 'id_username'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter password',
            'class': 'input-field',
            'id': 'id_password'
        })