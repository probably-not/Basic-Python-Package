class BaseConfig(object):
    """The BaseConfig class for the application."""
    CONFIG_TYPE = 'Base'

class DevelopmentConfig(BaseConfig):
    """The DevelopmentConfig class, which is used to configure the application while in development."""
    CONFIG_TYPE = 'Development'

class ProductionConfig(BaseConfig):
    """The ProductionConfig class, which is used to configure the application while in production."""
    CONFIG_TYPE = 'Production'
