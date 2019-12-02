from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')), 
    path(
      'admin/password_reset/',
       auth_views.PasswordResetView.as_view(),
       name='admin_password_reset',
     ),
    path(
         'admin/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done',
     ),
    path(
         'reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm',
     ),
    path(
         'reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete',
     ),

    path('',include('Articles.urls', namespace='Articles')),
    path('',include('Events.urls', namespace='Events')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# <appname>/templates/admin/my_custom_index.html

admin.site.site_header = "Enterpreneur Network Administration"
admin.site.site_title = "Enterpreneur Network Admin"
admin.site.index_title = "Welcome to Admin Page"

