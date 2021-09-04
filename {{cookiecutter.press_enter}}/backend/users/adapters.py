from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest
import environ

env = environ.Env()
ENVIRONEMT = env('ENVIRONMENT')

class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def get_email_confirmation_url(self, request, emailconfirmation):
        current_site = f'https://{{cookiecutter.domain_name}}'
        if ENVIRONEMT == 'local':
            current_site = 'http://0.0.0.0:8000'
        return f'{current_site}/api/confirm-email/{emailconfirmation.key}/'


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
