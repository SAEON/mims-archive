from pathlib import Path

from flask import Flask

from mims.ui.archive import views
from mims.ui.archive.config import config
from odp.const import ODPArchive, ODPScope
from odp.const.hydra import HydraScope
from odp.ui import base


def create_app():
    """
    Flask application factory.
    """
    app = Flask(__name__)
    app.config.update(
        ARCHIVE_ID=ODPArchive.MIMS_ARCHIVE,
        UI_CLIENT_ID=config.MIMS.ARCHIVE.UI_CLIENT_ID,
        UI_CLIENT_SECRET=config.MIMS.ARCHIVE.UI_CLIENT_SECRET,
        UI_CLIENT_SCOPE=[
            HydraScope.OPENID,
            HydraScope.OFFLINE_ACCESS,
            ODPScope.ARCHIVE_READ,
            ODPScope.PACKAGE_READ,
            ODPScope.PACKAGE_WRITE,
            ODPScope.RESOURCE_READ,
            ODPScope.RESOURCE_WRITE,
            ODPScope.TOKEN_READ,
        ],
        SECRET_KEY=config.MIMS.ARCHIVE.FLASK_SECRET,
    )

    base.init_app(
        app,
        user_api=True,
        client_api=False,
        template_dir=Path(__file__).parent / 'templates',
    )
    views.init_app(app)

    return app
