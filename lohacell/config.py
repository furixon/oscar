from django.apps import apps
from oscar.core.application import OscarConfig

class Shop(OscarConfig):
    name = 'oscar2'

    def ready(self):
        self.catalogue_app = apps.get_app_config('catalog2')
        self.basket_app = apps.get_app_config('basket')
        # ...

    def get_urls(self):
        urls = [
            path('catalog2/', self.catalogue_app.urls),
            path('basket/', self.basket_app.urls),
            # ...
        ]