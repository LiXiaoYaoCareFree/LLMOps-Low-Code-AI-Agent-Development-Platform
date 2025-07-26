from api.pkg.sqlalchemy import SQLAlchemy
from injector import Module, Binder
from flask_migrate import Migrate
from api.internal.extension.migrate_extension import migrate
from api.internal.extension.database_extension import db


class ExtensionModule(Module):
    """Extension module for dependency injection."""
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)