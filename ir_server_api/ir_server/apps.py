from django.apps import AppConfig


class ir_serverConfig(AppConfig):
    name = "ir_server"

    def ready(self):
        from .ap_scheduler import start

        start()
