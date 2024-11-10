import importlib

if "bpy" in locals():
    importlib.reload(ui)
    importlib.reload(operators)
    importlib.reload(utilities)
    
    importlib.reload(arm_left)
    importlib.reload(arm_right)

    importlib.reload(leg_left)
    importlib.reload(leg_right)

    importlib.reload(finger_1_left)
    importlib.reload(finger_2_left)
    importlib.reload(finger_3_left)
    importlib.reload(finger_4_left)
    importlib.reload(finger_5_left)
    
    importlib.reload(finger_1_right)
    importlib.reload(finger_2_right)
    importlib.reload(finger_3_right)
    importlib.reload(finger_4_right)
    importlib.reload(finger_5_right)

else:
    from . import (
        ui,
        operators,
        utilities,
        
        arm_left,
        arm_right,

        leg_left,
        leg_right,
        
        finger_1_left,
        finger_2_left,
        finger_3_left,
        finger_4_left,
        finger_5_left,
        
        finger_1_right,
        finger_2_right,
        finger_3_right,
        finger_4_right,
        finger_5_right
    )

modules = (
    ui,
    operators,
    utilities,
    
    arm_left,
    arm_right,
    
    leg_left,
    leg_right,
    
    finger_1_left,
    finger_2_left,
    finger_3_left,
    finger_4_left,
    finger_5_left,
    
    finger_1_right,
    finger_2_right,
    finger_3_right,
    finger_4_right,
    finger_5_right
)

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in reversed(modules):
        mod.unregister()