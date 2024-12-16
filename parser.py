import yaml
from dacite import from_dict, Config
from typing import Type, TypeVar, Any
import sys
from pathlib import Path

T = TypeVar('T')  # 任意のクラスをサポートするためのジェネリック型

class YamlParser:
    def __init__(self, config: Config | None = None):
        """
        YamlParserの初期化
        :param config: daciteのConfigオブジェクト（デフォルトはNone）
        """
        self.config = config or Config()

    def parse(self, yaml_path: str, cls: Type[T]) -> T:
        """
        YAMLをパースして指定されたクラスにマッピングする。
        :param yaml_path: YAMLファイルのパス
        :param cls: マッピング対象のクラス
        :return: 指定されたクラスのインスタンス
        """
        with open(yaml_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
        
        return from_dict(data_class=cls, data=yaml_data, config=self.config)

# サンプルクラス
from dataclasses import dataclass

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
class AConfig:
    database: DatabaseConfig
    server: ServerConfig
    logging: LoggingConfig
    features: FeaturesConfig

# 使用例
if __name__ == "__main__":
    parser = YamlParser()
    
    # サンプルYAMLファイル
    yaml_content = """
    name: MyApplication
    version: "1.0.0"
    debug: true
    """
    if getattr(sys, 'frozen', False):
        current_dir = Path(sys.executable).parent
    else:
        current_dir = Path(__file__).parent
    config_path = (current_dir / ".." / "resources" / "config.yml").resolve()
    # st.write(f"{config_path=}")
    # YAMLファイルを一時的に保存
    yaml_file_path = config_path
    # with open(yaml_file_path, "w") as file:
    #     file.write(yaml_content)

    # YAMLをパースしてAppConfigクラスにマッピング
    config = parser.parse(yaml_file_path, AConfig)
    print(config)
