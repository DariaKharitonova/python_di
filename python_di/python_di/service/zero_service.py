from python_di.context.context import Context


class ZeroService:
    def __init__(self):
        self._data: list = [1, 6, 8]

    def do_something(self) -> list:
        context = Context()
        svc = context.get_service_by_name('OneService')
        print(f'Some number from OneService is {svc.number}')
        return self._data
