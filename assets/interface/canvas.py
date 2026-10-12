# assets/interface/canvas.py

from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtCore import Qt
from assets.interface.wires import Pin, Wire

class Canvas(QGraphicsView):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 2000, 2000)
        self.setScene(self.scene)

        self.setRenderHint(self.renderHints().Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        self.current_wire = None

    def mousePressEvent(self, event):
        position = self.mapToScene(event.pos())
        item = self.scene.itemAt(position, self.transform())

        if isinstance(item, Pin):
            if item.output:
                self.current_wire = Wire(item)
                self.scene.addItem(self.current_wire)
                item.wires.append(self.current_wire)
                return
                
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.current_wire:
            self.current_wire.end_position = self.mapToScene(event.pos())
            self.current_wire.update_path()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.current_wire:
            scene_pos = self.mapToScene(event.pos())
            item = self.scene.itemAt(scene_pos, self.transform())

            if isinstance(item, Pin) and not item.output and len(item.wires) == 0:
                self.current_wire.end = item
                item.wires.append(self.current_wire)
                self.current_wire.update_path()
            else:
                self.current_wire.start.wires.remove(self.current_wire)
                self.scene.removeItem(self.current_wire)
                
            self.current_wire = None
        else:
            super().mouseReleaseEvent(event)