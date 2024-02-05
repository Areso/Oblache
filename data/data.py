from dataclasses import dataclass
from datetime import datetime

time = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))


@dataclass
class MySqlData:
    host: str = None
    port: int = 3306
    user: str = None
    database: str = None
    password: str = None
