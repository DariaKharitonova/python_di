from python_di.service.one_service import OneService


class TwoService:
    def __init__(self, first_service: OneService):
        self._first_service = first_service

    def say_bye(self) -> str:
        name = self._first_service.get_name()
        msg = f'Bye from {name} and TwoService'
        print(msg)
        return msg
