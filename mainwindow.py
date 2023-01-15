from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("Universe")

        #Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        settings_menu = menu_bar.addMenu("&Settings")
        help_menu = menu_bar.addMenu("&Help")



        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)


        about_action = help_menu.addAction("About")
        about_action.setStatusTip("About KAtomic")
        about_action.triggered.connect(self.button_clicked_about)

    def button1_clicked(self):
        print("clicked on the button")

    # About Button
    def button_clicked_about(self):
        ret = QMessageBox.about(self,"About Universe",
                                        "Universe is your hub to speed up your workflow.")
        if ret == QMessageBox.Ok :
            print("User chose OK")
        else :
            print ("User chose Cancel")

    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app")
