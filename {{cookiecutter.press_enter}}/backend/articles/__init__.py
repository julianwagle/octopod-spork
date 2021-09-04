from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'backend.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import backend.articles.signals


default_app_config = 'backend.articles.ArticlesAppConfig'
