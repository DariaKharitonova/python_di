class OneService:
    def __init__(self):
        self.name = 'OneService'
        self.number = 5

    def get_name(self) -> str:
        return self.name

    def say_hi(self) -> str:
        print(f'Hi from {self.name}')
        return 'Hi'
