from python_di.context.context import Context
from python_di.service.zero_service import ZeroService
from python_di.service.one_service import OneService
from python_di.service.two_service import TwoService


def init_context() -> Context:
    context = Context()
    context.add_service(ZeroService)
    context.add_service(OneService)
    context.add_service(TwoService)
    return context
