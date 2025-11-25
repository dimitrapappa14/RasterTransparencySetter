import os
from qgis.PyQt.QtWidgets import QAction, QInputDialog, QMessageBox
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsRasterLayer

class RasterTransparencySetterwithclick:
    def __init__(self, iface):
        self.iface = iface
        self.action = None

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        self.action = QAction(QIcon(icon_path), "Set Raster Transparency (Selected Layers)", self.iface.mainWindow())
        self.action.triggered.connect(self.set_transparency)
        self.iface.addPluginToMenu("&Raster Tools", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removePluginMenu("&Raster Tools", self.action)
        self.iface.removeToolBarIcon(self.action)

    def set_transparency(self):
        selected_layers = self.iface.layerTreeView().selectedLayers()
        if not selected_layers:
            QMessageBox.information(self.iface.mainWindow(), "No Layers Selected", "Please select one or more layers first.")
            return

        raster_layers = [layer for layer in selected_layers if isinstance(layer, QgsRasterLayer)]
        if not raster_layers:
            QMessageBox.information(self.iface.mainWindow(), "No Raster Layers Selected", "No selected layers are raster layers.")
            return
        
        value, ok = QInputDialog.getInt(
            self.iface.mainWindow(),
            "Set Raster Transparency",
            "Enter transparency (0–100%):",
            50, 0, 100
        )
        if ok:
            opacity = value / 100.0
            for layer in raster_layers:
                layer.renderer().setOpacity(opacity)
                layer.triggerRepaint()
