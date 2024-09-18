from threading import Thread

from app.src.domain.interfaces.usecases.usecase_interface import UseCaseInterface


class UseCaseThread:

    def __init__(self, usecase: UseCaseInterface):
        self.usecase = usecase
        self.running = False

    def __run_usecase(self):
        try:
            self.running = True
            self.usecase.execute()
            self.running = False
        except Exception as e:
            self.running = False
            print(e)

    def start(self):
        self.thread = Thread(target=self.__run_usecase)
        self.thread.start()
        return self.thread

    def join(self):
        self.thread.join()

    def is_running(self):
        return self.running
