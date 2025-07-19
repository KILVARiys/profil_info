import sys
from PySide6.QtWidgets import QApplication
from gui.gui import Widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Widget()
    window.resize(1280, 720)
    window.setStyleSheet("background-color: #ffffff;")
    window.show()

    try:
        with open("style.qss", "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)
    except Exception as e:
        print("Файл стилей не найден:", e)

    sys.exit(app.exec())