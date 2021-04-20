from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit
import sys
from PySide2.QtGui import QIcon, QFont
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Simple Notepad Application")
        self.setGeometry(300,200,1280,600)
 
        self.textEdit = QTextEdit(self)
        self.textEdit.setFont(QFont('Sanserif', 13))
        self.setCentralWidget(self.textEdit)
 
        self.setIcon()
 
        self.create_menu()
        self.show()
 
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
 
    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        editMenu = mainMenu.addMenu('Edit')
        fontMenu = mainMenu.addMenu('Font')
        helpMenu = mainMenu.addMenu('Help')
 
        openAction = QAction(QIcon('open.png'), "Open", self)
        openAction.setShortcut('Ctrl+O')
 
        saveAction = QAction(QIcon('save.png'), "Save", self)
        saveAction.setShortcut('Ctrl+S')
 
        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut('Ctrl+X')
 
        exitAction.triggered.connect(self.exit_app)
 
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
 
    def exit_app(self):
        self.close()
 
 
myapp = QApplication(sys.argv)
window = Window()
 
myapp.exec_()
sys.exit()
