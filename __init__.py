"""
Copyright (c) 2021 Korobanov Konstantin

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

bl_info = {
    "name": "Vertex Randomiser",
    "description": (
        "Module randomise shift of selected in object edit mode vertices "
        "location to random value. User can passed random shift value "
        "scoup for each location vectors values."
    ),
    "author": "Diarts",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "N > Misc",
    "support": "COMMUNITY",
    "category": "Update Mesh",
}


if "bpy" in locals():
    import importlib
    importlib.reload(core)
else:
    from vertex_randomiser import core

from bpy import utils
from bpy.types import Scene
from bpy.props import PointerProperty

from .core.properties import VertexRandom
from .core.panels import VertexRandomNPanel, VertexRandomToolsPanel
from .core.operators import BRandomiseVertices

# ------------------------------------------------------------------

def register()->None:
    """Register blender UI classes."""

    _classes_register()

    for label in ("x", "y", "z"):
        _properties_add_to_scene(label)

def unregister()->None:
    """Root Unregister blender UI classes method."""

    _classes_unregister()

def _classes_register()->None:
    """Root register blender UI classes method."""

    utils.register_class(VertexRandom)
    utils.register_class(BRandomiseVertices)
    utils.register_class(VertexRandomNPanel)
    utils.register_class(VertexRandomToolsPanel)

def _classes_unregister()->None:
    """Removed blender UI classes."""

    for label in ("x", "y", "z"):
        _remove_properties_from_scene(label)

    utils.unregister_class(VertexRandomToolsPanel)
    utils.unregister_class(VertexRandomNPanel)
    utils.unregister_class(BRandomiseVertices)
    utils.unregister_class(VertexRandom)


def _properties_add_to_scene(label: str)->None:
    """Add properties to blender scene by label."""

    setattr(Scene, f"{label}_randomiser", PointerProperty(type=VertexRandom))

def _remove_properties_from_scene(label: str)->None:
    """Remove properties from blender scene by label."""

    delattr(Scene, f"{label}_randomiser")

if __name__ == "__main__":
    register()