from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from random import randint
class Inserter():
    names = ["Paco","Pepa","Pipo","Popi"]
    limit = 0
    def __init__(self) -> None:
        
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("alumnos.sqlite")
        self.db.open()
    def insert(self):
        if self.limit != 0:
            for i in range(0,self.limit):
                self.crearAlumno()            
    def chooseRandomFromList(self,list):
        return list[randint(0,len(list)-1)]
    def crearAlumno(self):
        nombre = self.chooseRandomFromList(self.names)
        nota1Ev = randint(0,10)
        nota2Ev = randint(0,10)
        nota3Ev = randint(0,10)
        id = self.getID() + 1
        print(id)
        query = QSqlQuery(f"""INSERT INTO alumnos VALUES(
            {id},
            '{nombre}',
            {nota1Ev},
            {nota2Ev},
            {nota3Ev})""",db=self.db)
        print(query.exec_())
    def getID(self):
        query = QSqlQuery("SELECT MAX(id) FROM alumnos",db=self.db)
        query.next()
        id = query.value(0)
        return id
