from parserPHP import analizar_sintactico, analizar_semantico
from lexerPHP import analizar_lexico
import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMenuBar, QTextEdit, QPushButton, QGroupBox, QLabel, QStatusBar
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('GUI - Analizador Léxico, Sintáctico y Semántico - PHP')

        # Menú
        menubar = self.menuBar()
        menu_principal = menubar.addMenu('Menu Principal')
        menu_ayuda = menubar.addMenu('Ayuda')

        # Layout principal
        main_layout = QVBoxLayout()

        # Área de texto
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText('Escriba su expresión aquí...')
        main_layout.addWidget(self.text_area)

        # Botones
        button_layout = QHBoxLayout()

        btn_lexico = QPushButton('ANÁLISIS LÉXICO')
        btn_lexico.setStyleSheet('background-color: lightgreen')
        btn_lexico.clicked.connect(self.analisis_lexico)

        btn_sintactico = QPushButton('ANÁLISIS SINTÁCTICO')
        btn_sintactico.setStyleSheet('background-color: khaki')
        btn_sintactico.clicked.connect(self.analisis_sintactico)

        btn_semantico = QPushButton('ANÁLISIS SEMÁNTICO')
        btn_semantico.setStyleSheet('background-color: lightblue')
        btn_semantico.clicked.connect(self.analisis_semantico)

        btn_limpiar = QPushButton('LIMPIAR PANTALLA')
        btn_limpiar.clicked.connect(self.limpiar_pantalla)

        button_layout.addWidget(btn_lexico)
        button_layout.addWidget(btn_sintactico)
        button_layout.addWidget(btn_semantico)
        button_layout.addWidget(btn_limpiar)

        main_layout.addLayout(button_layout)

        # Output
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        main_layout.addWidget(QLabel('Output'))
        main_layout.addWidget(self.output_area)

        # Estado
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Labels de estado y tipo de análisis
        self.estado_label = QLabel('Estado: Listo')
        self.tipo_analisis_label = QLabel('Tipo Análisis: N/A')
        main_layout.addWidget(self.estado_label)
        main_layout.addWidget(self.tipo_analisis_label)

        # Configurar layout central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def actualizar_estado(self):
        self.estado_label.setText('Estado: Listo')

    def analisis_lexico(self):
        self.limpiar_pantalla()
        self.estado_label.setText('Estado: En proceso')
        self.tipo_analisis_label.setText('Tipo Análisis: Léxico')
        self.status_bar.showMessage('Estado: Análisis Léxico en proceso...', 5000)
        analizar_lexico(self.text_area.toPlainText())
        for line in self.abrir_archivo('lexico.txt'):
            self.output_area.append(line)
        QTimer.singleShot(5000, self.actualizar_estado)

    def analisis_sintactico(self):
        self.limpiar_pantalla()
        self.estado_label.setText('Estado: En proceso')
        self.tipo_analisis_label.setText('Tipo Análisis: Sintáctico')
        self.status_bar.showMessage('Estado: Análisis Sintáctico en proceso...', 5000)
        analizar_sintactico(self.text_area.toPlainText())
        for line in self.abrir_archivo('sintactico.txt'):
            self.output_area.append(line)
        QTimer.singleShot(5000, self.actualizar_estado)

    def analisis_semantico(self):
        self.limpiar_pantalla()
        self.estado_label.setText('Estado: En proceso')
        self.tipo_analisis_label.setText('Tipo Análisis: Semántico')
        self.status_bar.showMessage('Estado: Análisis Semántico en proceso...', 5000)
        analizar_semantico(self.text_area.toPlainText())
        for line in self.abrir_archivo('semantico.txt'):
            self.output_area.append(line)
        QTimer.singleShot(5000, self.actualizar_estado)

    def limpiar_pantalla(self):
        self.output_area.clear()
        self.estado_label.setText('Estado: Listo')
        self.tipo_analisis_label.setText('Tipo Análisis: N/A')
        self.status_bar.showMessage('Estado: Pantalla Limpiada', 5000)

    def abrir_archivo(self, log_file_name):
        script_dir = os.path.dirname(__file__)
        logs_dir = os.path.join(script_dir, 'logs')
        resultado = []
        with open(os.path.join(logs_dir, log_file_name), 'r', encoding='UTF-8') as log_file:    
            for line in log_file:
                resultado.append(line.strip())
        return resultado

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())