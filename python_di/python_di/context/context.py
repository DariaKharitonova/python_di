from typing import Any

from di import Container
from di.dependent import Dependent
from di.executors import SyncExecutor


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(
                *args,
                **kwargs,
            )
        return cls._instances[cls]


class Context(metaclass=Singleton):
    def __init__(self):
        self._container = Container()
        self._executor = SyncExecutor()
        self._solved = {}

    def add_service(self, service: Any):
        self._solved[service.__name__] = self._container.solve(
            Dependent(service, scope=service.__name__),
            scopes=[service.__name__]
        )

    def get_service_by_name(self, name: str) -> Any:
        solved = self._solved[name]
        with self._container.enter_scope(name) as state:
            return solved.execute_sync(
                executor=self._executor, state=state,
            )
