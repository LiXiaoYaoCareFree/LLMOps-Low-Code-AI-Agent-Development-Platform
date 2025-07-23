import dotenv
from flask_sqlalchemy import SQLAlchemy
from injector import Injector

from app.http.module import ExtensionModule
from internal.server.http import Http
from internal.router import Router
from config import Config

# 将env加载到环境变量中
dotenv.load_dotenv()

conf = Config()

injector = Injector([ExtensionModule])

app = Http(__name__,conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))


if __name__ == "__main__":
    app.run(debug=True)
