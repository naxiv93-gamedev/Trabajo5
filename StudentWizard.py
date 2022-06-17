import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWizard, QWizardPage, QLineEdit, QVBoxLayout, QLabel, QCheckBox, QComboBox, QRadioButton,QMessageBox, QWidget
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRelation, QSqlRelationalTableModel
import pyqtgraph as pg
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import pyqtgraph as pg
import pyqtgraph.exporters
from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
from reportlab.pdfgen.canvas import Canvas
from PySide6.QtWebEngineCore import QWebEngineSettings

class WizardPage1(QWizardPage):
    
    db = QSqlDatabase("QSQLITE")
    db.setDatabaseName("alumnos.sqlite")
    db.open()
    def __init__(self):
        super().__init__()
        self.selectorAlumno = QComboBox()
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        labelIncluirDatos = QLabel('Incluir datos de:')
        self.checkboxEv1 = QCheckBox('1ª Evaluacion')
        self.checkboxEv2 = QCheckBox('2ª Evaluacion')
        self.checkboxEv3 = QCheckBox('3ª Evaluacion')
        self.checkboxInforme = QCheckBox('Incluir gráfica de progreso')
        self.notas1Ev = -1
        self.notas2Ev = -1
        self.notas3Ev = -1
        self.notas = []
        self.evaluaciones = []
        vLayout1 = QVBoxLayout(self)
        vLayout1.addWidget(self.selectorAlumno)
        vLayout1.addWidget(labelIncluirDatos)
        vLayout1.addWidget(self.checkboxEv1)
        vLayout1.addWidget(self.checkboxEv2)
        vLayout1.addWidget(self.checkboxEv3)
        vLayout1.addWidget(self.checkboxInforme)
        self.selectorAlumno.currentIndexChanged.connect(self.checkAlumno)
        self.checkboxEv1.stateChanged.connect(self.checkCheckboxes)
        self.checkboxEv2.stateChanged.connect(self.checkCheckboxes)
        self.checkboxEv3.stateChanged.connect(self.checkCheckboxes)
        self.checkboxInforme.stateChanged.connect(self.checkCheckboxes)
        self.getAlumnos()
        
    def checkAlumno(self,index):
        self.graphWidget.clear()
        self.notas1Ev = -1
        self.notas2Ev = -1
        self.notas3Ev = -1        
        itemText = self.selectorAlumno.itemText(index)
        if itemText != "Seleccione un alumno":
            currentIndex = itemText.split("-")[0]
            query = QSqlQuery("SELECT * FROM Alumnos WHERE ID = "+currentIndex,db=self.db)
            query.next()
            self.nombre = query.value(1)
            self.notas1Ev = query.value(2)
            self.notas2Ev = query.value(3)
            self.notas3Ev = query.value(4)
            self.checkCheckboxes()
        self.completeChanged.emit()





            
    def checkCheckboxes(self):
        index = self.selectorAlumno.currentIndex()
        itemText = self.selectorAlumno.itemText(index)
        self.notas = []
        self.evaluaciones = []
        if itemText != "Seleccione un alumno":
            if self.checkboxEv1.isChecked():
                self.notas.append(self.notas1Ev)
                self.evaluaciones.append(1)
            if self.checkboxEv2.isChecked():
                self.notas.append(self.notas2Ev)
                self.evaluaciones.append(2)
            if self.checkboxEv3.isChecked():
                self.notas.append(self.notas3Ev)
                self.evaluaciones.append(3) 
            if self.checkboxInforme.isChecked():
                self.graphWidget.plot(self.evaluaciones,self.notas)
        self.completeChanged.emit()
    def getAlumnos(self):
        self.selectorAlumno.addItem("Seleccione un alumno")
        query = QSqlQuery("SELECT * FROM Alumnos",db=self.db)
        # Recorremos el resultado de esa query agregando al comboBox el listado de artistas
        while query.next():
            id = str(query.value(0))
            nombre = query.value(1)
            string = id + "-" + nombre
            self.selectorAlumno.addItem(string)
    def isComplete(self):
        return len(self.notas) >= 2 and super().isComplete() and self.selectorAlumno.currentIndex() != 0
        
class WizardPage2(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Generar Informe de Alumno")
        self.setSubTitle("Indique que hacer con el informe generado")
        self.radioButton1 = QRadioButton("Guardar en disco")
        self.radioButton2 = QRadioButton("Mostrar en pantalla")
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(self.radioButton1)
        vLayout.addWidget(self.radioButton2)
        self.setLayout(vLayout)
        self.radioButton1.toggled.connect(self.checking)
        self.radioButton2.toggled.connect(self.checking)
    def checking(self):
        self.completeChanged.emit()    
    def isComplete(self):
        return (self.radioButton1.isChecked() or self.radioButton2.isChecked()) and super().isComplete()

        
            
            
class StudentGenerationWizard(QWizard):
    
    def __init__(self):
        super().__init__()
        # Creamos un QWizard

        # Establecemos un estilo del QWizard
        self.setWizardStyle(QWizard.ModernStyle)

        # Se pueden ver los estilos en https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWizard.html#PySide6.QtWidgets.PySide6.QtWidgets.QWizard.setWizardStyle
        #self.wizard.setWizardStyle(QWizard.AeroStyle)
        #self.wizard.setWizardStyle(QWizard.ClassicStyle)
        #self.wizard.setWizardStyle(QWizard.MacStyle)



        # Un QWizard se compone de páginas QWizardPage con elementos: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWizard.html#elements-of-a-wizard-page
        self.page1 = WizardPage1()
        self.page1.setTitle('Generar Informe de Alumno')
        self.page1.setSubTitle('Seleccione El alumno del que desea crear el informe')
        
        
        # Añadimos la página al QWizard, como se hace con los widgets en los layouts
        self.addPage(self.page1)
        self.page2 = WizardPage2()
        self.addPage(self.page2)
        self.button(QWizard.FinishButton).clicked.connect(self.onFinish)
        
    def onFinish(self):
        outfile = "resultStudent.pdf"

        exporter = pg.exporters.ImageExporter(self.page1.graphWidget.plotItem)
        exporter.parameters()['width'] = 400
        exporter.export('graphic.png')
        template = PdfReader("templateStudent.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)
        canvas = Canvas(outfile)
        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)
        canvas.drawString(200,750,str(self.page1.nombre))
        mean = 0
        amt = 0
        if self.page1.checkboxEv1.isChecked():
            mean += self.page1.notas1Ev
            amt += 1
            canvas.drawString(305,660,str(self.page1.notas1Ev))

        if self.page1.checkboxEv2.isChecked():
            mean += self.page1.notas2Ev
            amt += 1
            canvas.drawString(305,635,str(self.page1.notas2Ev))
        if self.page1.checkboxEv3.isChecked():
            mean += self.page1.notas3Ev
            amt += 1
            canvas.drawString(305,610,str(self.page1.notas3Ev))
        mean = mean/amt
        canvas.drawString(305,586,str(mean))
        if self.page1.checkboxInforme.isChecked():
            canvas.drawImage("graphic.png", 50, 200, width=None,height=None,mask=None)
        canvas.save()
        if self.page2.radioButton1.isChecked():
            self.dlg = QMessageBox(self)
            self.dlg.setText("Se ha generado el informe. Se ubica en la propia carpeta de la aplicacion.")
            self.dlg.setStandardButtons(QMessageBox.Ok)
            button = self.dlg.exec() 
        else:
            self.dlg = QMessageBox(self)
            self.dlg.setText("Se ha generado el informe, el cual se mostrará a continuacion.")
            self.dlg.setStandardButtons(QMessageBox.Ok)
            button = self.dlg.exec() 
            self.viewWidget = ViewWidget()
            self.viewWidget.show()
            



class ViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Viewer")
        vbox = QVBoxLayout(self)
        self.setLayout(vbox)
        # QWebEngineView es una vista de una web (vista de un navegador incrustada en una app)
        # Documentación de la clase: https://doc.qt.io/qtforpython/PySide6/QtWebEngineWidgets/QWebEngineView.html
        self.web = QWebEngineView()
        vbox.addWidget(self.web)

        # Para mostrar un PDF, es necesario habilitar los plugins. Los plugins están en https://doc.qt.io/qtforpython/PySide6/QtWebEngineCore/QWebEngineSettings.html#detailed-description
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        # Con Path guardamos la ruta relativa al documento
        rutaConPDF = Path("resultStudent.pdf")
        # Cargamos el fichero con la ruta absoluta como uri
        # Usando http o https también se pueden cargar páginas web
        self.web.load(QUrl(rutaConPDF.absolute().as_uri()))

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StudentGenerationWizard()
    window.show()
    app.exec()