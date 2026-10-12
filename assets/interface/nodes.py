# assets/interface/node_test.py

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt

class LogicGateNode(QGraphicsRectItem):
    logic_gate_width = 100
    logic_gate_height = 60

    def __init__(self, logic_gate: str, x: float, y: float, color: str = "#000000"):
        super().__init__(0, 0, self.logic_gate_width, self.logic_gate_height)
        self.setPos(x, y)
        self.logic_gate = logic_gate

        self.setFlags(
            QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable
        )

        self.setBrush(QBrush(QColor("#222222")))
        self.setPen(QPen(QColor(color)))