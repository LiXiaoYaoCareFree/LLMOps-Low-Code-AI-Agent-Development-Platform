import dotenv
from api.pkg.sqlalchemy import SQLAlchemy
from injector import Injector
from flask_migrate import Migrate

from api.app.http.module import ExtensionModule
from api.internal.server.http import Http
from api.internal.router import Router
from api.config import Config

# 将env加载到环境变量中
dotenv.load_dotenv()

conf = Config()

injector = Injector([ExtensionModule])

app = Http(__name__,
           conf=conf,
           db=injector.get(SQLAlchemy),
           migrate=injector.get(Migrate),
           router=injector.get(Router)
)


if __name__ == "__main__":
    app.run(debug=True)
