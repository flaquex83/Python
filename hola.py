#tutorial de pyqt

from PyQt4.QtGui import *

import sys

class Ventana(QWidget):
	"""docstring for Ventana"""
	def __init__(self):
		super(Ventana, self).__init__()

		#cambiar el titulo de la ventana
		self.setWindowTitle("tutorial de Python con QT")

		#cambiar el tamano de la ventana
		self.resize(800, 600)

		#cambiar el icono de la ventana
		self.setWindowIcon(QIcon("logo.jpg"))

		#creando botones
		btn_guardar = QPushButton("Guardar", self)
		btn_1 = QPushButton("1", self)
		btn_2 = QPushButton("2", self)
		btn_3 = QPushButton("3", self)
		btn_4 = QPushButton("4", self)

		#colocando label en el sistema
		mensaje = QLabel("Label", self)
		mensaje.move(200,0)

		#Layout tipo grilla que es el que me importa
		grilla = QGridLayout(self)
		grilla.addWidget(btn_1, 0, 0)
		grilla.addWidget(btn_2, 0, 1)
		grilla.addWidget(btn_3, 1, 0)
		grilla.addWidget(btn_4, 1, 1)

app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec_())