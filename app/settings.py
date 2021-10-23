from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = "mariadb+mariadbconnector://db:db@127.0.0.1:3306/db"
