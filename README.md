# Raster Transparency Setter (Selected Layers)

A QGIS plugin that lets you quickly set the transparency (opacity) of **all selected raster layers** at once.

Instead of changing opacity one layer at a time, you simply select multiple raster layers in the **Layers Panel**, run the tool, and apply a percentage-based transparency to all of them in a single step.

---

## Features

- Works on **selected layers** in the QGIS Layers Panel.
- Automatically filters and applies changes **only to raster layers**.
- Ignores non-raster layers (vectors, groups, etc.).
- Simple dialog to set transparency between **0–100%**.
- Instant map refresh using `layer.triggerRepaint()`.

---

## Installation

1. **Download or clone** this repository.

2. Copy the plugin folder into your QGIS user plugins directory:

   - **Windows**  
     `C:\Users\<USERNAME>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\`

   - **Linux**  
     `~/.local/share/QGIS/QGIS3\profiles\default\python\plugins\`

   - **macOS**  
     `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`

3. Make sure the plugin folder name is something like:

   ```text
   RasterTransparencySetterwithclick
