from flask import Flask


def init_app(app: Flask):
    from . import home
    from odp.ui.base.views import archive, packages

    app.register_blueprint(home.bp)
    app.register_blueprint(archive.bp, url_prefix='/index')
    app.register_blueprint(packages.bp, url_prefix='/upload')
