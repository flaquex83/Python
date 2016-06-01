from PyQt4.QtGui import *
from subprocess import Popen
import sys

class Ventana(QWidget):
	"""docstring for Ventana"""
	def __init__(self):
		
		super(Ventana, self).__init__()
		
		#creacion de layout
		caja = QVBoxLayout(self)

		#creacion de los Widget de la aplicacion
		self.comboBox = QComboBox()
		#realizar lista  para el combobox
		lista = ['Seleccionar...','boleta','factura','nota de credito','nota de debito']

		for item in lista:
			self.comboBox.addItem(item)

		self.texto = QLineEdit()
		self.mensaje1 = QLabel('')
		self.mensaje1.hide()

		self.mensaje2 = QLabel('')

		caja.addWidget(self.comboBox)
		caja.addWidget(self.texto)
		caja.addWidget(self.mensaje1)
		caja.addWidget(self.mensaje2)

		self.setLayout(caja) # asi es como se setea el layout


		#ahora vamos por las conexiones 
		self.comboBox.currentIndexChanged.connect(self.combobox)
		self.texto.textChanged.connect(self.lineaTexto)

	def combobox(self):
		self.mensaje1.setText(self.comboBox.currentText())
		self.mensaje1.show()
		QMenssageBox.information(self, "Error", "Existe un problema en el sistema")

	def lineaTexto(self):
		self.mensaje2.setText(self.texto.text())

app = QApplication(sys.argv)

ventana = Ventana()
ventana.show()

sys.exit(app.exec_())