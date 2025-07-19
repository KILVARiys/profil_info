import os
from PySide6.QtWidgets import (
    QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QLineEdit
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QColor, QIcon


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        # Получаем путь к текущей директории
        base_path = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_path, "icons", "")

        # --- Боковая панель с меню ---
        self.menu_widget = QListWidget()
        self.menu_widget.setIconSize(QSize(48, 48))
        
        cs = QListWidgetItem(" CS 2")
        cs.setIcon(QIcon(icon_path + "cs2.jpg"))
        cs.setBackground(QColor("#CC8400"))
        cs.setTextAlignment(Qt.AlignCenter)

        dota = QListWidgetItem(" Dota 2")
        dota.setIcon(QIcon(icon_path + "dota2.jpg"))
        dota.setBackground(QColor("#5A0000"))
        dota.setTextAlignment(Qt.AlignCenter)

        rust = QListWidgetItem(" Rust")
        rust.setIcon(QIcon(icon_path + "rust.jpg"))
        rust.setBackground(QColor("#B30000"))
        rust.setTextAlignment(Qt.AlignCenter)

        steam = QListWidgetItem(" Steam")
        steam.setIcon(QIcon(icon_path + "steam.png"))
        steam.setBackground(QColor("#242C37"))
        steam.setTextAlignment(Qt.AlignCenter)

        # Добавляем элементы по одному
        self.menu_widget.addItem(cs)
        self.menu_widget.addItem(dota)
        self.menu_widget.addItem(rust)
        self.menu_widget.addItem(steam)

        for i in range(self.menu_widget.count()):
            item = self.menu_widget.item(i)
            item.setTextAlignment(Qt.AlignCenter)

        # --- Кнопка в верхней части окна ---
        self.toggle_button = QPushButton()
        self.toggle_button.setIcon(QIcon(icon_path + "menu.png"))  # Указываем иконку menu.png
        self.toggle_button.setIconSize(QSize(32, 32))
        self.toggle_button.setFixedSize(48, 48)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(True)
        self.toggle_button.toggled.connect(self.toggle_menu)

        # --- Верхнее поле поиска ---
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Введите ссылку на профиль steam")

        self.search_button = QPushButton("Поиск")
        self.search_button.setObjectName("search_button")
        self.search_button.setFixedHeight(57)

        # Горизонтальный макет для поиска
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)

        # --- Основное содержимое справа ---
        self.text_widget = QLabel("Null")

        content_layout = QVBoxLayout()
        content_layout.addLayout(search_layout)     # Поле ввода + кнопка сверху
        content_layout.addWidget(self.text_widget)  # Текст ниже
        content_layout.addStretch()                 # Освобождает пространство внизу

        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        # --- Макет боковой панели (чтобы можно было скрыть/показать) ---
        side_layout = QVBoxLayout()
        side_layout.addWidget(self.menu_widget)
        side_layout.setContentsMargins(0, 0, 0, 0)
        side_layout.setSpacing(0)

        side_widget = QWidget()
        side_widget.setLayout(side_layout)

        # --- Основной макет окна ---
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- Верхняя панель с кнопкой меню ---
        top_toolbar = QHBoxLayout()
        top_toolbar.addWidget(self.toggle_button)
        top_toolbar.addStretch()

        main_layout.addLayout(top_toolbar)

        # --- Горизонтальный макет: боковая панель + основное содержимое ---
        layout = QHBoxLayout()
        layout.addWidget(side_widget, 1)
        layout.addWidget(main_widget, 4)

        main_layout.addLayout(layout)

        self.setLayout(main_layout)

    def toggle_menu(self, checked):
        self.menu_widget.setVisible(checked)