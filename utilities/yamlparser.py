# from pathlib import Path
from yaml import safe_load, unsafe_load, full_load, load
import yaml
from pathlib import Path
import streamlit as st
from dacite import from_dict
from dataclasses import dataclass
import sys

if getattr(sys, 'frozen', False):
    current_dir = Path(sys.executable).parent
else:
    current_dir = Path(__file__).parent
config_path = (current_dir / ".." / "resources" / "config.yml").resolve()
st.write(f"{config_path=}")

@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    name: str

@dataclass
class ServerConfig:
    host: str
    port: int

@dataclass
class LoggingConfig:
    level: str
    file: str

@dataclass
class FeaturesConfig:
    enable_feature_x: bool
    enable_feature_y: bool

@dataclass
class Config:
    database: DatabaseConfig
    server: ServerConfig
    logging: LoggingConfig
    features: FeaturesConfig

    # def __repr__(self):
    #     return f"AppConfig(host={self.host}, port={self.port},\
    #             username={self.username}, password={self.password}, name={self.name})"

def read_yaml():
    st.write(f"{config_path=}")
    with config_path.open() as f:
        data = load(f,Loader=yaml.FullLoader)
        print(data)
        config = from_dict(data_class=Config, data=data)
        print(config)
        return config

