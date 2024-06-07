import os

class AppConfig():
    def __init__(self) -> None:
        self.DB_SERVER = "sqlite:///kanban-board.db"
        # os.environ.get("KEY")


class AppTestConfig(AppConfig):
    def __init__(self) -> None:
        super().__init__()
        self.DB_SERVER = "sqlite:///:memory:"

# test_config = AppTestConfig()