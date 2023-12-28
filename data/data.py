from dataclasses import dataclass


@dataclass
class MySqlData:
    host: str = None
    port: int = 3306
    user: str = None
    database: str = None
    password: str = None
