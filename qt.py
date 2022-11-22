from PySide2 import *

def main():
    app= QApplication()
    window= Window()

    

    window.show()
    status= app.exec_()
    sys.exit(status)