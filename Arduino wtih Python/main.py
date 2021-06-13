from pyfirmata import Arduino, util
from time import sleep
# import serial # used for serial monitor communication
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
import sys


class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
                                                # x ranges from 0-1920
                                                # y ranges from 0-1080 (for HD displays)
        self.setGeometry(200, 200, 400, 600) # x, y, width, height
        self.setWindowTitle("My first GUI")
        self.initUI()
        self.b1flag = 0 # status flag ofr b1, 0 for un-clicked, 1 for clicked
        self.b2flag = 0
        self.port = 'COM3' # com port for the Arduino
        self.board = Arduino(self.port)

    def initBoard(self):
        iterator = util.Iterator(self.board)
        iterator.start()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)  # set where the label goes
        self.label.setText("Hello World!")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)  # set where the button goes
        self.b1.setText("CLICK ME!")
        self.b1.move(50, 70)
        self.b1.clicked.connect(self.b1clicked)

        self.b2 = QtWidgets.QPushButton(self)  # set where the button goes
        self.b2.setText("LED on 8")
        self.b2.move(50, 100 )
        self.b2.clicked.connect(self.b2clicked)

        self.slider = QtWidgets.QSlider(Qt.Horizontal, self)
        # QtWidgets.QSlider(Qt.Vertical)
        self.slider.setGeometry(50, 150, 100, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(3)
        self.slider.setValue(1)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.value_changed)

    def b1clicked(self):
        print("a")
        self.b1flag = not self.b1flag
        print("b")
        if self.b1flag:
            print("d")
            self.b1.setText("I have been clicked")
            self.update()
        else:
            self.b1.setText("I have been unclicked")
            self.update()

    def b2clicked(self):
        # print("a")
        self.b2flag = not self.b2flag
        # print("b")
        if self.b2flag:
            # print("d")
            self.b2.setText("2 ON")
            self.board.digital[8].write(1) # sets pin 8 to high (1)
            self.update()
        else:
            self.b2.setText("2 OFF")
            self.board.digital[8].write(0) # sets pin 8 to low (0)
            self.update()

    def value_changed(self, i):
        print(i)
        if i == 1:
            self.board.digital[9].write(1)
            self.board.digital[10].write(0)
            self.board.digital[11].write(0)
        elif i == 2:
            self.board.digital[9].write(1)
            self.board.digital[10].write(1)
            self.board.digital[11].write(0)
        elif i == 3:
            self.board.digital[9].write(1)
            self.board.digital[10].write(1)
            self.board.digital[11].write(1)
        else:
            self.board.digital[9].write(0)
            self.board.digital[10].write(0)
            self.board.digital[11].write(0)


    def update(self):
        self.b1.adjustSize() # update the button width when the text changes
        self.b2.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = myWindow()

    # port = 'COM3' # com port for the Arduino
    #
    # board = Arduino(port)
    #
    # iterator = util.Iterator(board)
    # iterator.start()

    # while True:
    #     board.digital[8].write(1)
    #     sleep(1)
    #     board.digital[8].write(0)
    #     sleep(1)



    win.show()
    sys.exit(app.exec_()) # handles app termination


window()




