# Bundles all routes into an import package

from .admin_routes import admin_blueprint
from .curator_routes import curator_blueprint
from .enduser_routes import enduser_blueprint

__all__ = ["admin_blueprint", "curator_blueprint", "enduser_blueprint"]
