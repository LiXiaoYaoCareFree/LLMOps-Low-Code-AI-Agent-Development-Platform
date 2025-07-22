from flask import Flask


from internal.router import Router
from config import Config

class Http(Flask):
    """Http服务引擎"""
    def __init__(self, *args,conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_router(self)

        self.config.from_object(conf)
