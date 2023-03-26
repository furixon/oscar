from oscar import config

class Lohacell(config.Shop):
    # Override get_urls method
    def get_urls(self):
        urlpatterns = [
            path('catalog2/', self.catalogue_app.urls),
            # all the remaining URLs, removed for simplicity
            # ...
        ]
        return urlpatterns