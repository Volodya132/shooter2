from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, \
    QHBoxLayout, QVBoxLayout, QFormLayout

import json

app = QApplication([])

'''Замітки в json'''
notes = {
    "Ласкаво просимо!": {
        "текст": "Це найкращий додаток для заміток у світі!",
        "теги": ["добро", "інструкція"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file)