bl_info = {
    "name": "Bone Snapper",
    "description": "This addon brings bone snapping techniques, including IK to FK and vice versa functionality to Blender.",
    "author": "Ali3n Systems, eEight",
    "version": (1, 0),
    "blender": (4, 2, 1),
    "warning": "This addon is still in alpha so expect performance issues, also please report any bugs or submit PRs on the github page.",
}

import importlib

if "load_modules" in locals():
    importlib.reload(load_modules)
else:
    from . import load_modules

def register():
    load_modules.register()

def unregister():
    load_modules.unregister()

if __name__ == "__main__":
    register()

