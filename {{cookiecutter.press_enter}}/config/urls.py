
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from django.conf.urls import include
from django.views.generic import RedirectView

from backend.rest_auth.views import ( 
    PasswordResetView,
    PasswordResetConfirmView,
    LoginView,
    LogoutView,
    UserDetailsView,
    PasswordChangeView
)
from backend.rest_auth.registration.views import (
    RegisterView,
    ResendEmailVerificationView,
    VerifyEmailView
)

urlpatterns = [

    # URLs that do not require a session or valid token
    path('api/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('api/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('api/users/login/', LoginView.as_view(), name='rest_login'),
    # # URLs that require a user to be logged in with a valid session / token.
    path('api/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('api/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

    # URLs with views located in rest_auth/registration
    path('api/users/', RegisterView.as_view(), name='rest_register'),
    path('api/resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('api/confirm-email/<key>/', VerifyEmailView.as_view(), name='email_verification_sent'),


    path('account/', include('allauth.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),

    # path("api/auth-token/", obtain_auth_token),
    path('api/', include('backend.articles.urls', namespace='articles')),
    path('api/', include('backend.profiles.urls', namespace='profiles')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
