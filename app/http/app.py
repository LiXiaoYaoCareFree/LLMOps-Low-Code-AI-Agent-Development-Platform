import dotenv
from injector import Injector

from internal.server.http import Http
from internal.router import Router

# 将env加载到环境变量中
dotenv.load_dotenv()
injector = Injector()

app = Http(__name__, router=injector.get(Router))


if __name__ == "__main__":
    app.run(debug=True)
