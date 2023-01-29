from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

def upload_profile_photo(request):
    form = forms.UploadProfilPhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilPhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/photo_profil_upload.html', context={'form': form})

