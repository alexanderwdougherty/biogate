# assets/interface/window.py

from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QTextEdit
from assets.interface.canvas import Canvas
from assets.interface.nodes import LogicGateNode

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biogate")
        self.resize(1100, 700)

        widget = QWidget()
        self.setCentralWidget(widget)
        
        main_layout = QVBoxLayout(widget)
        logic_gate_bar_layout = QHBoxLayout()

        logic_gates = {
            "AND": "#00cc00",
            "OR": "#00cccc",
            "NOT": "#cc0000",
            "NAND": "#cccc00",
            "NOR": "#0000cc",
            "XOR": "#cc00cc",
            "XNOT": "#cccccc"
                       }

        for gate, color in logic_gates.items():
            button = QPushButton(f"+{gate}")
            button.clicked.connect(lambda checked = False, g = gate, c = color: self.spawn_node(g, c))
            logic_gate_bar_layout.addWidget(button)

        self.canvas = Canvas()

        main_layout.addWidget(self.canvas, 3)
        main_layout.addLayout(logic_gate_bar_layout, 1)


    def spawn_node(self, logic_gate: str, color: str):
        center = self.canvas.mapToScene(self.canvas.viewport().rect().center())
        node = LogicGateNode(logic_gate, center.x() - (LogicGateNode.logic_gate_width / 2), center.y() - (LogicGateNode.logic_gate_height / 2), color)
        self.canvas.scene.addItem(node)
