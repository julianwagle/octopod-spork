from django.urls import path

from .views import RegisterView, VerifyEmailView, ResendEmailVerificationView


urlpatterns = [
    path('', RegisterView.as_view(), name='rest_register'),
    path('verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('resend-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    # This url is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint w proper key.
    # re_path(
    #     r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
    #     name='account_confirm_email',
    # ),
    # https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path('confirm-email/<key>/', VerifyEmailView.as_view(), name='email_verification_sent'),
]
