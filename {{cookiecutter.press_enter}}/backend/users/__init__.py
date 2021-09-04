from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "backend.users"
    label = 'users'
    verbose_name = _("Users")

    def ready(self):
        import backend.users.signals  # noqa F401


# This is how we register our custom app config with Django. Django is smart
# enough to look for the `default_app_config` property of each registered app
# and use the correct app config based on that value.
default_app_config = 'backend.users.UsersAppConfig'
