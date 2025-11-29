# Bundles all routes into an import package

from .auth_routes import auth_blueprint
from .admin_routes import admin_blueprint
from .curator_routes import curator_blueprint
from .enduser_routes import enduser_blueprint

__all__ = [
    "auth_blueprint",
    "admin_blueprint",
    "curator_blueprint",
    "enduser_blueprint",
]
