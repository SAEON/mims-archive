from odp.config.base import BaseConfig
from odp.config.mixins import AppConfigMixin


class MIMSArchiveConfig(BaseConfig, AppConfigMixin):
    class Config:
        env_prefix = 'MIMS_ARCHIVE_'


class MIMSConfig(BaseConfig):
    _subconfig = {
        'ARCHIVE': MIMSArchiveConfig,
    }


class Config(BaseConfig):
    _subconfig = {
        'MIMS': MIMSConfig,
    }


config = Config()
