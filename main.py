import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from PySide6.QtCore import Qt
from ui_mainMenu import Ui_MainWindow
from PySide6.QtWidgets import QWidget

from ModifyAlumno import ModifyAlumno
from DeleteAlumno import DeleteAlumno
from NewAlumno import NewAlumno
from ReadAlumno import ReadAlumno
from StudentWizard import StudentGenerationWizard
from ClassWizard import ClassGenerationWizard






class MainWindow(QMainWindow, Ui_MainWindow):
    modify = None
    new = None
    delete = None
    read = None
    studentForm = None
    classForm = None
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        self.actionMostrar_alumno.triggered.connect(self.mostrar)
        self.actionA_adir_nuevo_alumno.triggered.connect(self.nuevo)
        self.actionBorrar_alumno.triggered.connect(self.borrar)
        self.actionModificar_alumno.triggered.connect(self.modificar)
        
        self.botonLeerAlumno.clicked.connect(self.mostrar)
        self.botonCrearAlumno.clicked.connect(self.nuevo)
        self.botonEliminarAlumno.clicked.connect(self.borrar)
        self.botonModificarAlumno.clicked.connect(self.modificar)
        self.botonGenerarInformeAlumno.clicked.connect(self.informeEstudiante)
        self.botonGenerarInformeClase.clicked.connect(self.informeClase)
        self.botonCerrar.clicked.connect(self.close)
        
    def mostrar(self):
        self.read = ReadAlumno()
        self.read.show()
    def nuevo(self):
        self.new = NewAlumno()
        self.new.show()
    def borrar(self):
        self.delete = DeleteAlumno()
        self.delete.show()
    def modificar(self):
        self.modify = ModifyAlumno()
        self.modify.show()
    def informeEstudiante(self):
        self.studentForm = StudentGenerationWizard()
        self.studentForm.show()
    def informeClase(self):
        self.classForm = ClassGenerationWizard()
        self.classForm.show()
    

    
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
