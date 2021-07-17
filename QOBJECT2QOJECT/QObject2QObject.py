from PyQt5.QtCore import *


class Send_Tester(QObject):

    custom_signal = pyqtSignal(str)

    def send_signal(self):

        message = "hello world ! "
        print("send", message)
        self.custom_signal.emit(message)


class Recv_Tester(QObject):

    @pyqtSlot(str)
    def recv_signal(self, message):
        print("recved ! -> ", message )


if __name__ == '__main__':

    send_tester = Send_Tester()
    recv_tester = Recv_Tester()

    send_tester.custom_signal.connect(recv_tester.recv_signal)

    send_iteration_count = 10

    for i in range(send_iteration_count):

        print("iteration count -> ", i)
        send_tester.send_signal()