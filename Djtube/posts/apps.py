from django.apps import AppConfig


class PostsAppConfig(AppConfig):
    name = "posts"

    def ready(self):
        from .signals.post_save import post_save_post