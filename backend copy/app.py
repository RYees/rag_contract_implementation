from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from ragbackend import settings

class Rags(Flask):
    """A custom Flask app for Rag"""

    def __init__(self, *args, **kwargs):
        # kwargs.update(
        #     {
        #         "template_folder": settings.FLASK_TEMPLATE_PATH,
        #         "static_folder": settings.STATIC_ASSETS_PATH,
        #         "static_url_path": "/static",
        #     }
        # )
        super(Rags, self).__init__(__name__, *args, **kwargs)
        # Make sure we get the right referral address even behind proxies like nginx.
        self.wsgi_app = ProxyFix(self.wsgi_app, x_for=settings.PROXIES_COUNT, x_host=1)
        # Configure Redash using our settings
        self.config.from_object("main.settings")


def create_app():
    from . import (
        main
    )  

    app = Rags()

    main.init_app(app)

    return app
