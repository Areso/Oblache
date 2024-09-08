import os
from datetime import datetime
import time
import allure
from locust import task, constant_pacing, HttpUser, LoadTestShape
import random
from config import cfg, logger
from tests_api.utils.checking import Checking
import assertion


class TosUser(HttpUser):
    wait_time = constant_pacing(cfg.pacing_sec)
    host = cfg.api_host
    token = None

    @staticmethod
    def get_token(get_token):
        TosUser.token = get_token[0]
        assert TosUser.token is not None, 'Token is None.'

    @task
    def get_tos(self):
        headers = {'Content-Type': 'application/json'}
        with self.client.get("/tos", headers=headers, catch_response=True) as response:
            if response.status_code == 200:
                print(f'correct status code: {response.status_code}')
            else:
                response.failure(f'Incorrect status code {response.status_code}')
                print(f'Incorrect status code: {response.status_code}')

    def on_stop(self):
        attach = r'C:\Users\User\PycharmProjects\locust\my_report1.html'
        allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.HTML)
        logger.debug(f"user stopped")


class StagesShape(LoadTestShape):
    stages = [
        {"duration": 10, "users": 5, "spawn_rate": 1},
        {"duration": 20, "users": 10, "spawn_rate": 1},
        {"duration": 30, "users": 20, "spawn_rate": 1},
        {"duration": 20, "users": 10, "spawn_rate": 1},
        {"duration": 10, "users": 5, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None


if __name__ == "__main__":
    # Получите текущее время в формате ЧЧММСС
    current_time = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))

    # Используйте текущее время в имени файла
    # report_file_name = f"my_report_{current_time}.html"
    report_file_name = f"my_report1.html"

    # Запустите Locust с вашим файлом и именем отчёта
    os.system(f"locust -f try_perfomance.py --headless -u 10 -r 10 --run-time 15s --html={report_file_name}")
