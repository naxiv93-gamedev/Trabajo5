from statistics import mean
from PySide6.QtWidgets import QWidget
from ui_deleteAlumno import Ui_DeleteAlumno
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel


class DeleteAlumno(QWidget,Ui_DeleteAlumno):
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
        self.botonConfirmar.clicked.connect(self.deleteAlumno)
        
        
    def deleteAlumno(self):
        
        itemText = self.selectorAlumno.itemText(self.selectorAlumno.currentIndex())
        if(itemText == "Seleccione un alumno"):
            self.close()
        id  =  itemText.split("-")[0]
        query = QSqlQuery("DELETE FROM alumnos WHERE id ="+id,db=self.db)
        query.exec_()
        
        self.close()
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
        else:
            self.labelNombre.setText("")
            self.labelEv1.setText("")
            self.labelEv2.setText("")
            self.labelEv3.setText("")
            self.labelMedia.setText("")
            
    