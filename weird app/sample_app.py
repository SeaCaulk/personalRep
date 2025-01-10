from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QToolBar, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)
        self.label = QLabel("Hello, World")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.layout.addWidget(self.label)
        self._createMenuBar()
        self._createToolBars()
        self.buttonpush()

    def _createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")

    def _createToolBars(self):
        # Using a title
        fileToolBar = self.addToolBar("File")
        # Using a QToolBar object

    def buttonpush(self):
        button = QPushButton("Click Me", self)
        self.layout.addWidget(button)
        button.clicked.connect(clickeed)
def clickeed():
    print("clicked with utter success.")
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()