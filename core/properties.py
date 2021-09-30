from bpy.types import PropertyGroup
from bpy.props import FloatProperty

__all__ = (
    "VertexRandom",
)

class VertexRandom(PropertyGroup):
    """Class contain properties of vertex randomisation configuration."""

    random_min: FloatProperty(
        name="min_value",
        description="Minimal random value.",
        default=0,
    )
    random_max: FloatProperty(
        name="max_value", 
        description="Maximum random value.",
        default=0,
    )
