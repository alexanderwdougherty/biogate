# assets/interface/window.py

from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QTextEdit
from assets.interface.canvas import Canvas
from assets.interface.nodes import LogicGateNode
import assets.config

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biogate")
        self.resize(1100, 700)

        widget = QWidget()
        self.setCentralWidget(widget)
        
        main_layout = QVBoxLayout(widget)
        logic_gate_bar_layout = QHBoxLayout()

        for gate, config in assets.config.LOGIC_GATES.items():
            color, inputs, outputs = config
            button = QPushButton(f"+{gate}")
            button.clicked.connect(lambda checked = False, g = gate, c = color, i = inputs, o = outputs: self.spawn_node(g, c, i, o))
            logic_gate_bar_layout.addWidget(button)

        self.canvas = Canvas()

        main_layout.addWidget(self.canvas, 3)
        main_layout.addLayout(logic_gate_bar_layout, 1)


    def spawn_node(self, logic_gate: str, color: str, inputs: int, outputs: int):
        center = self.canvas.mapToScene(self.canvas.viewport().rect().center())

        node = LogicGateNode(
            logic_gate,
            center.x() - (LogicGateNode.logic_gate_width / 2), 
            center.y() - (LogicGateNode.logic_gate_height / 2), 
            color = color,
            inputs = inputs,
            outputs = outputs
        )
        self.canvas.scene.addItem(node)
