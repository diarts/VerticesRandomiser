__all__ = (
    "ObjectInteractionMode",
    "PanelOptions",
    "PanelSpaceType",
    "PanelRegionType",
    "PanelContextType",
)

class ObjectInteractionMode:
    """Blender interaction with object mode."""
    EDIT_MESH: str = "EDIT_MESH"

class PanelOptions:
    """Common blender UI panel options."""
    DEFAULT_CLOSED: str = "DEFAULT_CLOSED"
    HEADER_LAYOUT_EXPAND: str = "HEADER_LAYOUT_EXPAND"

class PanelSpaceType:
    """Panel UI type."""
    VIEW_3D: str = "VIEW_3D"
    PROPERTIES: str = "PROPERTIES"

class PanelRegionType:
    """Panel UI location."""
    UI: str = "UI"
    WINDOW: str = "WINDOW"

class PanelContextType:
    """Panel context for some space types."""
    OBJECT: str = "object"
