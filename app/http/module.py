from pkg.sqlalchemy import SQLAlchemy
from injector import Module, Binder

from internal.extension.database_extension import db


class ExtensionModule(Module):
    """Extension module for dependency injection."""
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)