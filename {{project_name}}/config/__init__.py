# Configuration Import
import os
if os.getenv('PROJECT_ENV', 'dev') == 'dev':
    from .config import DevelopmentConfig as Config
else:
    from .config import ProductionConfig as Config
