bl_info = {
    "name": "Vertices Randomiser",
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
    from . import core

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