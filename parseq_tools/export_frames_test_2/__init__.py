from . import info
from . import maths_operations
from . import camera_operations
from . import import_export

bl_info = {
    "name": "Export Camera Animation to Deforum collab/webui",
    "author": "Michael Walker (@mwalk10)",
    "version": (1, 2, 0),
    "blender": (3, 5, 1),
    "location": "File > Export > Diffusion Notebook String",
    "description": "Export camera animations formatted for use in Deforum: collab and Webui's",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export",
}

# Register and unregister methods
def register():
    import_export.register()

def unregister():
    import_export.unregister()
