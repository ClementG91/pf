from django.contrib.auth.decorators import login_required, permission_required
from . import forms, models
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
@login_required
@permission_required('portefolio.add_photo')
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'project/photo_project_upload.html', context={'form': form})

@login_required
@permission_required('portefolio.add_photo')
def project_upload(request):
    project_form = forms.ProjectForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        project_form = forms.ProjectForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([project_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            project = project_form.save(commit=False)
            project.author = request.user
            project.photo = photo
            project.save()
            return redirect('home')
    context = {
        'project_form': project_form,
        'photo_form': photo_form,
    }
    return render(request, 'project/create_project_post.html', context=context)

@login_required
def view_project(request, project_id):
    project = get_object_or_404(models.Project, id=project_id)
    return render(request, 'project/view_project.html', {'project': project})

def view_cv(request):
    return render(request, 'project/view_cv.html')

def project_feed(request):
    return render(request, 'project/project_feed.html')