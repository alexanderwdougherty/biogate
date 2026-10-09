# assets/interface/window.py

from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QTextEdit
from assets.interface.canvas import Canvas
from assets.interface.node_test import LogicGateNode

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biogate")
        self.resize(1100, 700)

        widget = QWidget()
        self.setCentralWidget(widget)
        
        main_layout = QHBoxLayout(widget)
        sidebar_layout = QVBoxLayout()

        sidebar_layout = QVBoxLayout()

        self.add_and_logic_gate = QPushButton("+AND")
        self.add_and_logic_gate.clicked.connect(lambda: self.spawn_node("AND"))
        sidebar_layout.addWidget(self.add_and_logic_gate)

        self.canvas = Canvas()

        main_layout.addLayout(sidebar_layout, 1)
        main_layout.addWidget(self.canvas, 3)


    def spawn_node(self, logic_gate: str):
        node = LogicGateNode(logic_gate, 150, 150)
        self.canvas.scene.addItem(node)
