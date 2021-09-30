from typing import Set

from bpy.types import UILayout, Panel, Context
from bpy.props import BoolProperty

from .consts import (
    ObjectInteractionMode,
    PanelOptions,
    PanelSpaceType,
    PanelRegionType,
    PanelContextType,
)

__all__ = (
    "VertexRandomNPanel",
    "VertexRandomToolsPanel",
)

class ABSVertexRandomPanel:
    """Base class of vertex random panel.

    Args:
        is_nullified: Property store global property of Panel. 
            It controlling nullifing of panel parameter values.

    """

    bl_label: str = "Vertex randomiser"
    bl_options: Set[str] = {
        PanelOptions.DEFAULT_CLOSED,
        PanelOptions.HEADER_LAYOUT_EXPAND,
    }

    is_nullified: BoolProperty(name="Nullified toggle") = True

    def draw(self, context: Context)->None:
        """Draw panel."""

        # Update global is nullified parameter to False.
        self.__class__.is_nullified = False

        layout: UILayout = self.layout

        # Add parameters properties in layout.
        for label in ("x", "y", "z"):
            self._random_params_register(context, layout, label)

        # Add button for starting randomise to layout.
        layout.operator("button.randomise_vertices", icon="MESH_CUBE", text="Randomise")

    @classmethod
    def poll(cls, context: Context) -> bool:
        """Blender check, generate class and draw it or not."""

        # Context mode is EDIT MESH, panel must be draw.
        if context.mode == ObjectInteractionMode.EDIT_MESH:
            return True

        # Other context modes, if parameters value is not nullified, do it.
        elif not cls.is_nullified:
            cls._nullify_properties(context)

        return False

    def _random_params_register(
        self, 
        context: Context, 
        layout: UILayout, 
        label: str
    ) -> None:
        """Register vertex parameters random properties."""

        # Generate column.
        params_column = layout.column(align=True)
        params_column.label(text=f"Vertex {label.upper()} randomiser")

        scene_randomiser = getattr(context.scene, f"{label.lower()}_randomiser")

        # Add properties.
        params_column.prop(scene_randomiser, "random_min")
        params_column.prop(scene_randomiser, "random_max")

    @classmethod
    def _nullify_properties(cls, context: Context) -> None:
        """Nuliffy properties values if mode was been switched."""

        # Nullify randomisers values.
        for label in ("x", "y", "z"):
            prop = getattr(context.scene, f"{label.lower()}_randomiser")
            if prop.random_min != 0 or prop.random_max != 0:
                context.scene.property_unset(f"{label.lower()}_randomiser")

        # Update global nullified parameters.
        cls.is_nullified = True

class VertexRandomNPanel(ABSVertexRandomPanel, Panel):
    """Vertex random panel for N menu."""

    bl_idname: str = "N_PT_vertex_randomiser"
    bl_space_type: str = PanelSpaceType.VIEW_3D
    bl_region_type: str = PanelRegionType.UI

class VertexRandomToolsPanel(ABSVertexRandomPanel, Panel):
    """Vertex random panel for TOOLS menu."""

    bl_idname: str = "TOOLS_PT_vertex_randomiser"
    bl_space_type: str = PanelSpaceType.PROPERTIES
    bl_region_type: str = PanelRegionType.WINDOW
    bl_context: str = PanelContextType.OBJECT
