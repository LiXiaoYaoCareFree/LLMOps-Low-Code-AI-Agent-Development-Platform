# 应用默认配置项
DEFAULT_CONFIG = {
    # wtf配置
    "WTF_CSRF_ENABLED": "False",
    "SECRET_KEY": "dev-secret-key",  

    # SQLAlchemy数据库配置
    "SQLALCHEMY_DATABASE_URI": "",
    "SQLALCHEMY_POOL_SIZE": 30,
    "SQLALCHEMY_POOL_RECYCLE": 3600,
    "SQLALCHEMY_ECHO": "True",
}