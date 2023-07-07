import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QMessageBox

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.gonderen = QLineEdit()
        self.alici = QLineEdit()
        self.konu = QLineEdit()
        self.mesaj = QTextEdit()
        self.ilet = QPushButton("Gönder")
        self.temizle = QPushButton("Temizle")

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ilet)

        v_box = QVBoxLayout()
        v_box.addWidget(QLabel("Gönderen:"))
        v_box.addWidget(self.gonderen)
        v_box.addWidget(QLabel("Alıcı:"))
        v_box.addWidget(self.alici)
        v_box.addWidget(QLabel("Konu:"))
        v_box.addWidget(self.konu)
        v_box.addWidget(QLabel("Mesaj:"))
        v_box.addWidget(self.mesaj)
        v_box.addLayout(h_box)
        self.setLayout(v_box)

        self.setWindowTitle("Email")

        self.temizle.clicked.connect(self.yazi_temizle)
        self.ilet.clicked.connect(self.mesaji_gonder)

        self.show()

    def yazi_temizle(self):
        self.gonderen.clear()
        self.alici.clear()
        self.konu.clear()
        self.mesaj.clear()

    def mesaji_gonder(self):
        QMessageBox.information(self, "Bilgi", "Gönder butonuna tıklandı!")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())