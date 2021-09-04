
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from django.conf.urls import include
from django.views.generic import RedirectView


urlpatterns = [
    path("api/", include("config.api_router")),

    path('api/', include('backend.rest_auth.urls')),
    # URLs that do not require a session or valid token
    # path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    # path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    # path('login/', LoginView.as_view(), name='rest_login'),
    # # URLs that require a user to be logged in with a valid session / token.
    # path('logout/', LogoutView.as_view(), name='rest_logout'),
    # path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    # path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),


    path('api/registration/', include('backend.rest_auth.registration.urls')),
    # path('', RegisterView.as_view(), name='rest_register'),
    # path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    # path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    # path('confirm-email/<key>/', VerifyEmailView.as_view(), name='email_verification_sent'),


    path('account/', include('allauth.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),

    # path("api/auth-token/", obtain_auth_token),
    path('api/', include('backend.articles.urls', namespace='articles')),
    path('api/', include('backend.profiles.urls', namespace='profiles')),

    # urls that don't perfectly adhere to realworld specs
    # path('users/', RegistrationAPIView.as_view()), => now api/registration
    # path('users/login/', LoginAPIView.as_view()), => now api/login

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
