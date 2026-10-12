# assets/interface/wires.py

from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsPathItem, QGraphicsItem
from PySide6.QtGui import QPen, QColor, QPainterPath
from PySide6.QtCore import QPointF, Qt
import assets.config

class Pin(QGraphicsEllipseItem):
    r = 5

    def __init__(self, parent, output = False):
        super().__init__(-self.r, -self.r, self.r * 2, self.r * 2, parent)
        self.parent = parent
        self.output = output
        self.wires = []

        self.setBrush(QColor("#ffffff"))
        self.setPen(QColor("#000000"))
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges)

    def position(self) -> QPointF:
        return self.mapToScene(QPointF(0, 0))

class Wire(QGraphicsPathItem):
    def __init__(self, start: Pin):
        super().__init__()
        self.start = start
        self.end = None
        self.end_position = start.position()

        self.setPen(QPen(QColor("#aaaaaa"), 3, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        self.setZValue(-1)

    def path(self):
        p1 = self.start.position()
        p2 = self.end.position() if self.end else self.end_position

        path = QPainterPath()
        path.moveTo(p1)

        dx = abs(p2.x() - p1.x()) / 2

        path.cubicTo(
            QPointF(p1.x() + dx, p1.y()),
            QPointF(p2.x() - dx, p2.y()),
            p2
        )
        self.setPath(path)