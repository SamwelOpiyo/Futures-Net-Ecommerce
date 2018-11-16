from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "futures_net_ecommerce.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
