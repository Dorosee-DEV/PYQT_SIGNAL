from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject


class Signal_Test(QObject):

    # QObject 를 상속받으면, 시그널을 생성할 수 있음
    custom_signal = pyqtSignal(str)

    def sendSign(self):
        message = "hello world ! "
        print("sended ! -> " , message)
        self.custom_signal.emit(message)


class Recv_Test(QObject):

    send_again_signal = pyqtSignal(str)

    def __init__(self):

        super(Recv_Test, self).__init__()

        self.one_more_tester = One_More_Test()
        self.send_again_signal.connect(self.one_more_tester.send_one_more)



    @pyqtSlot(str)
    def sendAgain(self, message):
        print("self again ! ", message)
        self.send_again_signal.emit(message)



class One_More_Test(QObject):

    one_more_sign = pyqtSignal(str)

    @pyqtSlot(str)
    def send_one_more(self,message):
        print("send one more !", message)



if __name__ == '__main__':

    signal_tester = Signal_Test()
    recv_tester = Recv_Test()
    signal_tester.custom_signal.connect(recv_tester.sendAgain)

    for i in range(5):
        print("iter -> ", i)
        signal_tester.sendSign()

