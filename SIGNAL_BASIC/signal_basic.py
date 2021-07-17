from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

class Signal_Test(QObject):

    # QObject 를 상속받으면, 시그널을 생성할 수 있음

    custom_signal = pyqtSignal(str)

    def sendSign(self):
        print("sended ! ")
        self.custom_signal.emit("hello world !")


@pyqtSlot(str)
def SignRecver(message):
    print("Recved Messege -> ", message)


if __name__ == '__main__':


    signal_tester = Signal_Test()
    signal_tester.custom_signal.connect(SignRecver)

    for i in range(5):
        print("iter -> ", i)
        signal_tester.sendSign()

