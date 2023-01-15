# Copyright (C) 2022 CJ (LinuxGamer)

# This file is part of Universe.

# Universe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Universe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Universe.  If not, see <http://www.gnu.org/licenses/>.

# Author: CJ (LinuxGamer), and others, see contributors list.

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
