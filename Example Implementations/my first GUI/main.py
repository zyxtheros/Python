from PyQt5 import QtWidgets
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

	def initUI(self):
		self.label = QtWidgets.QLabel(self)  # set where the label goes
		self.label.setText("Hello World!")
		self.label.move(50, 50)

		self.b1 = QtWidgets.QPushButton(self)  # set where the button goes
		self.b1.setText("CLICK ME!")
		self.b1.move(50, 75)
		self.b1.clicked.connect(self.clicked)

	def clicked(self):
		self.b1.setText("I have been clicked")
		self.update()

	def update(self):
		self.b1.adjustSize() # update the button width when the text changes


# def window():
# 	app = QApplication(sys.argv)
# 	win = myWindow()
# 
# 
# 
# 
# 
# 	win.show()
# 	sys.exit(app.exec_()) # handles app termination


# window()

class gridDemo(QWidget):
	def __init__(self):
		super().__init__()

		values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		positions = [(r, c) for r in range(3) for c in range(3)]

		layoutGrid = QGridLayout()
		self.setLayout(layoutGrid)

		for positions, value in zip(positions, values):
			print("coordinate:", str(positions), "with value", str(value))
			button = QPushButton(value)
			button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
			layoutGrid.addWidget(button, *positions)

def main():
	app = QApplication(sys.argv)

	demo = gridDemo()
	demo.show()

	sys.exit(app.exec_())

main()