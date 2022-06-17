
from msilib.schema import CheckBox
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
        self.setTitle('Generar Informe de Clase')
        self.setSubTitle('Seleccione la evaluacion y las opciones disponibles')
        alumnos = []
        labelNombreClase = QLabel('Nombre de la Clase:')
        self.nombreClase = QLineEdit()
        labelIncluirDatos = QLabel('Incluir datos de:')
        self.checkboxEv1 = QCheckBox('1ª Evaluacion')
        self.checkboxEv1.setChecked(True)
        self.checkboxEv2 = QCheckBox('2ª Evaluacion')
        self.checkboxEv2.setChecked(True)
        self.checkboxEv3 = QCheckBox('3ª Evaluacion')
        self.checkboxEv3.setChecked(True)
        labelOpcionesAvanzadas = QLabel('Opciones avanzadas:')

        self.checkboxAprobados = QCheckBox('Mostrar numero de Aprobados')
        self.checkboxAprobados.setChecked(True)
        self.checkboxSuspensos= QCheckBox('Mostrar numero de Suspensos')
        self.checkboxSuspensos.setChecked(True)
        self.checkboxPorcentaje = QCheckBox('Mostrar el porcentaje de Aprobados/Suspensos')
        self.checkboxPorcentaje.setChecked(True)
        self.notas1Ev = []
        self.notas2Ev = []
        self.notas3Ev = []
        self.evaluaciones = []
        vLayout1 = QVBoxLayout(self)
        vLayout1.addWidget(labelNombreClase)
        vLayout1.addWidget(self.nombreClase)
        vLayout1.addWidget(labelIncluirDatos)
        vLayout1.addWidget(self.checkboxEv1)
        vLayout1.addWidget(self.checkboxEv2)
        vLayout1.addWidget(self.checkboxEv3)
        vLayout1.addWidget(labelOpcionesAvanzadas)

        vLayout1.addWidget(self.checkboxAprobados)
        vLayout1.addWidget(self.checkboxSuspensos)
        vLayout1.addWidget(self.checkboxPorcentaje)
        
        
        self.checkboxEv1.stateChanged.connect(self.checkCheckboxes)
        self.checkboxEv2.stateChanged.connect(self.checkCheckboxes)
        self.checkboxEv3.stateChanged.connect(self.checkCheckboxes)
        self.checkboxAprobados.stateChanged.connect(self.checkCheckboxes)
        self.checkboxSuspensos.stateChanged.connect(self.checkCheckboxes)
        self.checkboxPorcentaje.stateChanged.connect(self.checkCheckboxes)
        self.nombreClase.textChanged.connect(self.completeChanged)
        self.checkCheckboxes()

        
        
   



            
    def checkCheckboxes(self):
        self.notas1Ev = []
        self.notas2Ev = []
        self.notas3Ev = []
        if self.checkboxEv1.isChecked():
            self.getNotas("nota1Ev",self.notas1Ev)
        if self.checkboxEv2.isChecked():
            self.getNotas("nota2Ev",self.notas2Ev)
        if self.checkboxEv3.isChecked():
            self.getNotas("nota3Ev",self.notas3Ev)
        self.completeChanged.emit()
    def getNotas(self,evaluacion,listaNotas):
        query = QSqlQuery(f"SELECT {evaluacion} FROM Alumnos",db=self.db)
        while query.next():
           listaNotas.append(query.value(0))
    def isComplete(self):
        return self.nombreClase.text() != "" and (len(self.notas1Ev)>0 or len(self.notas2Ev)>0 or len(self.notas3Ev)>0) and  (self.checkboxAprobados.isChecked() or self.checkboxSuspensos.isChecked()) and super().isComplete()
        
class WizardPage2(QWizardPage):
    def __init__(self):
        super().__init__()
        self.setTitle("Generar Informe de Clase")
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

        
            
            
class ClassGenerationWizard(QWizard):
    
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
        
        
        
        # Añadimos la página al QWizard, como se hace con los widgets en los layouts
        self.addPage(self.page1)
        self.page2 = WizardPage2()
        self.addPage(self.page2)
        self.button(QWizard.FinishButton).clicked.connect(self.onFinish)
        
    def onFinish(self):
        outfile = "resultClass.pdf"
        template = PdfReader("templateClass.pdf", decompress=False).pages[0]
        template_obj = pagexobj(template)
        canvas = Canvas(outfile)
        xobj_name = makerl(canvas, template_obj)
        canvas.doForm(xobj_name)
        canvas.drawString(200,750,str(self.page1.nombreClase.text()))
        if(self.page1.checkboxEv1.isChecked):
            if(self.page1.checkboxAprobados.isChecked()):
                canvas.drawString(400,630,str(self.getAprobados(self.page1.notas1Ev)))
                if(self.page1.checkboxPorcentaje.isChecked()):
                    canvas.drawString(400,605,str(int(self.getPorcentajeAprobados(self.page1.notas1Ev)))+"%")
            if(self.page1.checkboxSuspensos.isChecked()):
                canvas.drawString(400,580,str(self.getSuspensos(self.page1.notas1Ev)))
                if(self.page1.checkboxPorcentaje.isChecked()):
                    canvas.drawString(400,555,str(int(self.getPorcentajeSuspensos(self.page1.notas1Ev)))+"%")
            canvas.drawString(400,530,str(self.getMean(self.page1.notas1Ev)))
            
            
        if(self.page1.checkboxEv2.isChecked):
            if(self.page1.checkboxAprobados.isChecked()):
                canvas.drawString(400,430,str(self.getAprobados(self.page1.notas2Ev)))
                if(self.page1.checkboxPorcentaje.isChecked()):
                    canvas.drawString(400,405,str(int(self.getPorcentajeAprobados(self.page1.notas2Ev)))+"%")
            if(self.page1.checkboxSuspensos.isChecked()):
                canvas.drawString(400,380,str(self.getSuspensos(self.page1.notas2Ev)))
                if(self.page1.checkboxPorcentaje.isChecked()):
                    canvas.drawString(400,355,str(int(self.getPorcentajeSuspensos(self.page1.notas2Ev)))+"%")
            canvas.drawString(400,330,str(self.getMean(self.page1.notas2Ev)))
        
        if(self.page1.checkboxEv3.isChecked):
            if(self.page1.checkboxAprobados.isChecked()):
                canvas.drawString(400,230,str(self.getAprobados(self.page1.notas3Ev)))
                if(self.page1.checkboxPorcentaje.isChecked()):
                    canvas.drawString(400,205,str(int(self.getPorcentajeAprobados(self.page1.notas3Ev)))+"%")
            if(self.page1.checkboxSuspensos.isChecked()):
                canvas.drawString(400,180,str(self.getSuspensos(self.page1.notas2Ev)))
                if(self.page1.checkboxPorcentaje.isChecked()):
                    canvas.drawString(400,155,str(int(self.getPorcentajeSuspensos(self.page1.notas3Ev)))+"%")
            canvas.drawString(400,130,str(self.getMean(self.page1.notas3Ev)))    

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
    def getMean(self,listaNotas):
        mean = 0
        amt = 0
        for nota in listaNotas:
            mean += nota
            amt += 1
        return mean/amt
    def getAprobados(self,listaNotas):
        aprobados = 0
        for nota in listaNotas:
            if nota >= 5:
                aprobados += 1
        return aprobados
    def getSuspensos(self,listaNotas):
        return len(listaNotas) - self.getAprobados(listaNotas) 
    
    def getPorcentajeAprobados(self,listaNotas):
        return self.getAprobados(listaNotas)*100/len(listaNotas)
    
    def getPorcentajeSuspensos(self,listaNotas):
        return 100 - self.getPorcentajeAprobados(listaNotas)
    
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
        rutaConPDF = Path("resultClass.pdf")
        # Cargamos el fichero con la ruta absoluta como uri
        # Usando http o https también se pueden cargar páginas web
        self.web.load(QUrl(rutaConPDF.absolute().as_uri()))

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClassGenerationWizard()
    window.show()
    app.exec()