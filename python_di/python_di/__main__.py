from python_di.context.init_context import init_context


def main():
    print('start')
    context = init_context()
    first = context.get_service_by_name('OneService')
    second = context.get_service_by_name('TwoService')
    zero = context.get_service_by_name('ZeroService')

    first.say_hi()
    zero.do_something()
    second.say_bye()

    print('completed')


if __name__ == "__main__":
    main()
