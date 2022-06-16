from PySide6.QtWidgets import QWidget
from ui_newAlumno import Ui_NewAlumno
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel


class NewAlumno(QWidget,Ui_NewAlumno):
    db = QSqlDatabase("QSQLITE")
    db.setDatabaseName("alumnos.sqlite")
    db.open()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botonCancelar.clicked.connect(self.close)
        self.botonConfirmar.clicked.connect(self.crearAlumno)
    
    def crearAlumno(self):
        nombre = self.nombreAlumno.text()
        nota1Ev = self.notaEv1.value()
        nota2Ev = self.notaEv2.value()
        nota3Ev = self.notaEv3.value()
        id = self.getID() + 1
        query = QSqlQuery(db=self.db)
        query.prepare("INSERT INTO alumnos VALUES(:id,:nombre,:nota1,:nota2,:nota3)")
        query.bindValue(":id",id)
        query.bindValue(":nombre",nombre)
        query.bindValue(":nota1",nota1Ev)
        query.bindValue(":nota2",nota2Ev)
        query.bindValue(":nota3",nota3Ev)
        print(query.exec_())
        self.close()
    def getID(self):
        query = QSqlQuery("SELECT MAX(id) FROM alumnos",db=self.db)
        query.next()
        id = query.value(0)
        return id