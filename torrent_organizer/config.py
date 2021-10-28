from pydantic import BaseSettings, Field


class Config(BaseSettings):
    # source: str = Field(env="TORRENT_ORGANIZER_SOURCE")
    extensions: str = Field("mkv,mp4", env="TORRENT_ORGANIZER_EXTENSIONS")
    # destination: str = Field(env="TORRENT_ORGANIZER_DESTINATION")
    ignore_list = ["teaser", "spot", "trailer", "extra"]
