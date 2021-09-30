from random import uniform

from bpy.types import Operator, Context, Mesh
import bmesh
from bmesh.types import BMesh, BMVert

from .properties import VertexRandom

__all__ = (
    "BRandomiseVertices",
)

class BRandomiseVertices(Operator):
    """Vertex randomise button."""
    bl_description: str = "Randomise selected vertices."
    bl_idname: str = "button.randomise_vertices"
    bl_label: str = "Randomise Vertices"

    def execute(self, context: Context) -> None:
        """Randomise selected object selected verticles location parameters.
        """

        # Get object mesh.
        active_obj: Mesh = context.active_object.data
        obj_mesh: BMesh = bmesh.from_edit_mesh(active_obj)

        # Update selected verticles.
        for vertex in obj_mesh.verts:
            self._randomise_vertex(context, vertex)

        # Update real mesh.
        bmesh.update_edit_mesh(active_obj)

        return {"FINISHED"}

    def _randomise_vertex(self, context: Context, vertex:BMVert):
        """Randomise vertex location parameters."""

        # Skip not selected vertex.
        if not vertex.select:
            return

        # Go over vertex location parameters.
        for label in ("x", "y", "z"):
            label = label.lower()

            randomiser: VertexRandom = getattr(
                context.scene,
                 f"{label}_randomiser",
            )
            
            scale_value: float = uniform(
                randomiser.random_min, 
                randomiser.random_max,
            )
            
            current_value = getattr(vertex.co, label)
            setattr(vertex.co, label, current_value + scale_value)
