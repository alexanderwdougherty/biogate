# assets/interface/nodes.py

from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsItem
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt
from assets.interface.wires import Pin
import assets.config

class LogicGateNode(QGraphicsRectItem):
    logic_gate_width = 100
    logic_gate_height = 60

    def __init__(self, logic_gate: str, x: float, y: float, color: str = "#000000", inputs: int = 0, outputs: int = 0):
        super().__init__(0, 0, self.logic_gate_width, self.logic_gate_height)
        self.setPos(x, y)
        self.logic_gate = logic_gate
        self.pins = []

        gate = assets.config.LOGIC_GATES.get(self.logic_gate, ("#000000", 0, 0))

        color = color if color is not None else gate[0]
        inputs = inputs if inputs is not None else gate[1]
        outputs = outputs if outputs is not None else gate[2]

        self.setFlags(
            QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable |
            QGraphicsRectItem.GraphicsItemFlag.ItemSendsScenePositionChanges
        )

        self.setBrush(QBrush(QColor("#222222")))
        self.setPen(QPen(QColor(color), 2))

        self.add_pins(inputs, outputs)

    def add_pins(self, inputs: int, outputs: int):
        for i in range(inputs):
            in_pin = Pin(self, output = False)
            in_pin.setPos(0, self.logic_gate_height * (i + 1) / (inputs + 1))
            self.pins.append(in_pin)

        for i in range(outputs):
            out_pin = Pin(self, output = True)
            out_pin.setPos(self.logic_gate_width, self.logic_gate_height * (i + 1) / (outputs + 1))
            self.pins.append(out_pin)

    def itemChange(self, change, value):
        if change == QGraphicsItem.GraphicsItemChange.ItemPositionHasChanged:
                for pin in self.pins:
                      for wire in pin.wires:
                            wire.update_path()
        return super().itemChange(change, value)