from PySide6.QtWidgets import QWidget
from ui_modifyAlumno import Ui_ModifyAlumno
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
import pyqtgraph as pg

class ModifyAlumno(QWidget,Ui_ModifyAlumno):
    db = QSqlDatabase("QSQLITE")
    db.setDatabaseName("alumnos.sqlite")
    db.open()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectorAlumno.addItem("Seleccione un alumno")
        self.getAlumnos()
        self.selectorAlumno.currentIndexChanged.connect(self.mostrarAlumno)
        self.botonCancelar.clicked.connect(self.close)
        self.botonConfirmar.clicked.connect(self.modifyAlumno)
        self.notaEv1.valueChanged.connect(self.plot)
        self.notaEv2.valueChanged.connect(self.plot)
        self.notaEv3.valueChanged.connect(self.plot)

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
        if itemText != "Seleccione un alumno":
            id = self.getID(itemText)
            query = QSqlQuery("SELECT * FROM Alumnos WHERE ID = "+id,db=self.db)
            query.next()
            nombre = query.value(1)
            nota1Ev = query.value(2)
            nota2Ev = query.value(3)
            nota3Ev = query.value(4)
            self.nombreAlumno.setText(nombre)
            self.notaEv1.setValue(nota1Ev)
            self.notaEv2.setValue(nota2Ev)
            self.notaEv3.setValue(nota3Ev)
        else:
            self.nombreAlumno.setText("")
            self.notaEv1.setValue(0)
            self.notaEv2.setValue(0)
            self.notaEv3.setValue(0)
    def modifyAlumno(self):
        if(self.selectorAlumno.currentText() == "Seleccione un alumno"):
            self.close()
        itemText = self.selectorAlumno.itemText(self.selectorAlumno.currentIndex())
        id = self.getID(itemText)
        print(id)
        nombre = self.nombreAlumno.text()
        print(nombre)
        nota1Ev = self.notaEv1.value()
        print(nota1Ev)
        nota2Ev = self.notaEv2.value()
        print(nota2Ev)
        nota3Ev = self.notaEv3.value()
        print(nota3Ev)
        query = QSqlQuery(db=self.db)
        query.prepare("UPDATE alumnos SET nombre = :nombre , nota1Ev = :nota1 , nota2Ev = :nota2 , nota3Ev = :nota3  WHERE id = :id ");
        query.bindValue(":nombre", nombre);
        query.bindValue(":nota1", nota1Ev);
        query.bindValue(":nota2", nota2Ev);
        query.bindValue(":nota3", nota3Ev);
        query.bindValue(":id", id);
        print(query.exec_())
        self.close()
        
    def plot(self):
        self.graphWidget.clear()
        evaluaciones =[1,2,3]
        notas = [self.notaEv1.value(),self.notaEv2.value(),self.notaEv3.value()]
        self.graphWidget.plot(evaluaciones,notas)
    def getID(self,string):
        currentIndex = string.split("-")[0]
        return currentIndex

        
        