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

3. Restart QGIS.
4. Go to **Plugins → Manage and Install Plugins…**
5. In the **Installed** tab, find **RasterTransparencySetter** and check it to enable.         
     -----


     ## Usage

     1.**Prepare your Data**
     -Select multiple raster Layers.
     -Non-raster Layers (vector layers,groups etc ) wil be ignored.

     2.**Run the Plugin** ![icon icon ](icon.png)
    - From the menu: **Raster Tools → Set Raster Transparency (Selected Layers)**  
    - Or click the plugin **toolbar icon**

     3.**Set Transparency**  
    - A dialog box will appear asking:  
     > Enter transparency (0–100%):
    - Enter a value between **0% (fully opaque)** and **100% (fully transparent)**.  
    - Click **OK** to apply the transparency to all selected raster layers.  
    - Click **Cancel** if you do not want to make any changes.

     4.**View Changes**  
   - All selected raster layers will update immediately.  
   - The map canvas refreshes automatically with the new opacity values.

    ---
### Messages & Error Handling 

The plugin uses **QMessageBox** to show feedback direcctly in Qgis :

-**Info Messages:**
- If **no layers** are seleceted in the Layers Panel:
- “Please select one or more layers first.”
-If **none of the selected layers are raster layers**:
-“Please select one or more layers first.”

-**Input Dialog:** 
-Uses 'QInputDialog.getInt' to request a ytreansparency value between **0-100%**.
-If the user click **Cancel***, no changes are applied

- **Rendering update:**
  - After updating opacity, each raster layer is refreshed with:
    ```python
    layer.triggerRepaint()
    ```

---

## Limitations & Notes

- The plugin currently supports:
- Only **raster layers** (`QgsRasterLayer`).
- Any **non-raster layers** in the selection are ignored.

---
## License
This plugin is released under the GPL-3.0 license.
---
## Support and Contribution
- **Homepage**: [https://github.com/Consortis-Geospatial],(https://github.com/Consortis-Geospatial)
- **Author**: Dimitra Pappa -Consortis Geospatial
- **email**: pappa@consortis.gr
- **Repository**: [https://github.com/Consortis-Geospatial/SnapIntegrator],(https://github.com/Consortis-Geospatial/SnapIntegrator)
- **Issues Tracker**: [https://github.com/Consortis-Geospatial/SnapIntegrator],(https://github.com/Consortis-Geospatial//SnapIntegrator)
