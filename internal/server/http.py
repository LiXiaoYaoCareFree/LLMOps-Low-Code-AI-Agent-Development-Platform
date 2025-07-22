from flask import Flask


from internal.router import Router


class Http(Flask):
    """Http服务引擎"""
    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_router(self)
