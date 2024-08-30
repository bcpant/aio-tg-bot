from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

db_path = '/data/words_base.db'
user_answers = {}


class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()