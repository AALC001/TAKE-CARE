from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
     path('', admin.site.urls),
     path('reporting', LoginView.as_view(), name="login"),
     path('reporting', LogoutView.as_view(), name="logout"),
     path('reporting-Tool/', include('reportingTool.urls')),

     url(r'^archivage/', include('archivage.urls')),
     url(r'^api/', include('api.urls')),

     url(r'^', include("river_admin.urls")),
     path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset',),
     path('admin/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done',),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm',),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete',),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)