from PySide6.QtWidgets import  QApplication, QWidget
# from rockwidget import RockWidget
from mainwindow import MainWindow
# from msgbox import Widget
import sys

app = QApplication(sys.argv)

# window = RockWidget()
# window.show()

window = MainWindow(app)
window.show()

# window = Widget()
# window.show()

app.exec()
