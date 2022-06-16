from PySide6.QtWidgets import QWidget
from ui_readAlumno import Ui_ShowAlumno
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
import pyqtgraph as pg

class ReadAlumno(QWidget,Ui_ShowAlumno):
    db = QSqlDatabase("QSQLITE")
    db.setDatabaseName("alumnos.sqlite")
    db.open()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botonConfirmar.clicked.connect(self.close)
        self.selectorAlumno.addItem("Seleccione un alumno")
        self.getAlumnos()
        self.selectorAlumno.currentIndexChanged.connect(self.mostrarAlumno)

    def getAlumnos(self):
        query = QSqlQuery("SELECT * FROM Alumnos",db=self.db)
        # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
        while query.next():
            id = str(query.value(0))
            nombre = query.value(1)
            string = id + "-" + nombre
            self.selectorAlumno.addItem(string)
    def mostrarAlumno(self,index):
        itemText = self.selectorAlumno.itemText(index)
        self.graphWidget.clear()
        if itemText != "Seleccione un alumno":
            currentIndex = itemText.split("-")[0]
            query = QSqlQuery("SELECT * FROM Alumnos WHERE ID = "+currentIndex,db=self.db)
            query.next()
            nombre = query.value(1)
            nota1Ev = query.value(2)
            nota2Ev = query.value(3)
            nota3Ev = query.value(4)
            notaMedia = (nota1Ev+nota2Ev+nota3Ev)/3
            self.labelNombre.setText(nombre)
            self.labelEv1.setText(str(nota1Ev))
            self.labelEv2.setText(str(nota2Ev))
            self.labelEv3.setText(str(nota3Ev))
            self.labelMedia.setText(str(notaMedia))
            notas = [nota1Ev,nota2Ev,nota3Ev]
            evaluaciones = [1,2,3]
            self.graphWidget.plot(evaluaciones,notas)
            