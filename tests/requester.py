from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
from random import randint
class Requester():
    limit = 0
    def __init__(self) -> None:
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("alumnos.sqlite")
        self.db.open()
    def request(self):
        if self.limit != 0:
            for i in range(0,self.limit):
                query = QSqlQuery("SELECT * FROM alumnos",db=self.db)
                while query.next():
                    print(query.value(0),query.value(1),query.value(2),query.value(3),query.value(4))