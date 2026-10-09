# assets/interface/node_test.py

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt

class LogicGateNode(QGraphicsRectItem):
    def __init__(self, logic_gate: str, x: float, y: float):
        super().__init__(0, 0, 100, 60)
        self.setPos(x, y)
        self.logic_gate = logic_gate

        self.setFlags(
            QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable
        )

        self.setBrush(QBrush(QColor("#222222")))
        self.setPen(QPen(QColor("#00aaaa")))

        QGraphicsTextItem(logic_gate, self).setDefaultTextColor(Qt.GlobalColor.white)
        QGraphicsTextItem(logic_gate, self).setPos(30, 18)


