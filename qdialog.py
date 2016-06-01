from PyQt4.QtGui import *

import sys



#with open('signals.py','r') as f:
#	for l in f:
#		LINEA += 1
#
#	print LINEA

class Ventana(QDialog):
	"""docstring for Ventana"""
	def __init__(self):
		super(Ventana, self).__init__()

		self.setWindowTitle("Script de QDialog")
		self.lineas = 0
		#Creacion de Layout
		BoxVertical = QVBoxLayout(self)

		#creacion de los widget
		self.btn_abrir = QPushButton("Abrir")
		self.mensaje = QLabel("")
		self.mensaje.hide()

		BoxVertical.addWidget(self.btn_abrir)
		BoxVertical.addWidget(self.mensaje)

		self.setLayout(BoxVertical)

		self.btn_abrir.clicked.connect(self.abrirArchivo)

	def abrirArchivo(self):
		archivo = QFileDialog.getOpenFileName(self, "Abrir Archivo")
		self.calcularLinea(archivo)

	def calcularLinea(self, archivo):
		self.lineas = 0
		with open(archivo,'r') as f:
			for l in f:
				self.lineas += 1

		self.mensaje.setText(str(self.lineas))
		self.mensaje.show()


		
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()

sys.exit(app.exec_())