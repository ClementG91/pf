from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView)
import authentication.views, portefolio.views, project.views
import portefolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', portefolio.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('photo/upload/', portefolio.views.photo_upload, name='photo_upload'),
    path('photo/upload-multiple/', portefolio.views.create_multiple_photos, name='create_multiple_photos'),
    path('photo/upload/profil', authentication.views.upload_profile_photo, name='photo_profil_upload'),
    path('photo/<int:photo_id>', portefolio.views.view_photo, name='view_photo'),
    path('photo/<int:photo_id>/edit', portefolio.views.edit_photo, name='edit_photo'),
    path('photo-feed/', portefolio.views.photo_feed, name='photo_feed'),
    path('blog/create', portefolio.views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>', portefolio.views.view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit', portefolio.views.edit_blog, name='edit_blog'),
    path('follow-users/', portefolio.views.follow_users, name='follow_users'),
    path('photo/project/upload/', project.views.photo_upload, name='photo_project_upload'),
    path('project/create', project.views.project_upload, name='project_create'),
    path('project/<int:project_id>', project.views.view_project, name='view_project'),
    path('project-feed', project.views.project_feed, name='project_feed'),
    path('view-cv', project.views.view_cv, name='cv'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
