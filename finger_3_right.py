import bpy
from . import utilities

def draw_ui_finger_3_right(self, context, ik_to_fk_bone_objects, fk_to_ik_bone_objects):
    box = self.layout.column().box()
    if utilities.any_snapping_possible(ik_to_fk_bone_objects, fk_to_ik_bone_objects): 
        box.label(text = "Finger 3 Right Snapping", icon= 'SNAP_ON')
        if not all(ik_to_fk_bone_objects) and not all(fk_to_ik_bone_objects):
            box.label(text = "Bone Unavailable", icon= 'ERROR')
        else:
            grid = box.grid_flow(columns=2, align=True)   
            if all(ik_to_fk_bone_objects):
                grid.prop(context.scene.finger_3_right, 'ik_to_fk_toggle', toggle= True, text ="IK to FK")
            else:
                box.label(text = "IK to FK Unavailable", icon= 'ERROR')
            if all(fk_to_ik_bone_objects):
                grid.prop(context.scene.finger_3_right, 'fk_to_ik_toggle', toggle= True, text ="FK to IK")
            else:
                box.label(text = "FK to IK Unavailable", icon= 'ERROR')
    else:
        self.layout.column().label(text ="Active skeleton has no similar bones", icon='ERROR')

def ik_to_fk_bone_objects():
    ik_to_fk_bone_objects = {
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_3_ik_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_3_fk_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_2_pole_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_2_fk_right)
        }
    return ik_to_fk_bone_objects

def fk_to_ik_bone_objects():
    fk_to_ik_bone_objects = {
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_1_mch_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_2_mch_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_3_mch_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_1_fk_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_2_fk_right),
        bpy.context.active_object.pose.bones.get(bpy.context.scene.finger_3_3_fk_right)
        }
    return fk_to_ik_bone_objects

def ik_to_fk_bone_names(context):
    ik_to_fk_bone_names = [
        context.scene.finger_3_2_pole_right,
        context.scene.finger_3_3_ik_right,
        context.scene.finger_3_2_fk_right,
        context.scene.finger_3_3_fk_right
        ]
    return ik_to_fk_bone_names

def fk_to_ik_bone_names(context):
    fk_to_ik_bone_names = [
        context.scene.finger_3_1_fk_right,
        context.scene.finger_3_2_fk_right,
        context.scene.finger_3_3_fk_right,
        context.scene.finger_3_1_mch_right,
        context.scene.finger_3_2_mch_right,
        context.scene.finger_3_3_mch_right
        ]
    return fk_to_ik_bone_names

def ik_to_fk_snap(finger_3_2_pole_right, finger_3_3_ik_right, finger_3_2_fk_right, finger_3_3_fk_right): 
    finger_3_2_pole_right.matrix = finger_3_2_fk_right.matrix.copy()
    finger_3_3_ik_right.matrix = finger_3_3_fk_right.matrix.copy()      

def fk_to_ik_snap(finger_3_1_fk_right, finger_3_2_fk_right, finger_3_3_fk_right, finger_3_1_mch_right, finger_3_2_mch_right, finger_3_3_mch_right):
    finger_3_1_fk_right.matrix = finger_3_1_mch_right.matrix.copy()
    finger_3_2_fk_right.matrix = finger_3_2_mch_right.matrix.copy()
    finger_3_3_fk_right.matrix = finger_3_3_mch_right.matrix.copy()

def ik_to_fk_check(context):
    ik_to_fk_check = utilities.get_bones_with_check(context, ik_to_fk_bone_names(context))
    return ik_to_fk_check

def fk_to_ik_check(context):
    fk_to_ik_check = utilities.get_bones_with_check(context, fk_to_ik_bone_names(context))
    return fk_to_ik_check

def ik_to_fk_update(self, context):
    if self.ik_to_fk_toggle == True:
        bpy.ops.finger_3_right.operator_finger_3_right('INVOKE_DEFAULT')
    return

def fk_to_ik_update(self, context):
    if self.fk_to_ik_toggle == True:
        bpy.ops.finger_3_right.operator_finger_3_right('INVOKE_DEFAULT')
    return

class PropertiesFinger3Right(bpy.types.PropertyGroup):
    ik_to_fk_toggle: bpy.props.BoolProperty(default = False, update = ik_to_fk_update)
    fk_to_ik_toggle: bpy.props.BoolProperty(default = False, update = fk_to_ik_update)

class OperatorFinger3Right(bpy.types.Operator):
    bl_idname = "finger_3_right.operator_finger_3_right"
    bl_label = "Operator Finger 3 Right"

    _timer = None
    def modal(self, context, event):
        if event.type == 'TIMER':
            if context.scene.finger_3_right.fk_to_ik_toggle == True:
                fk_to_ik_snap(*fk_to_ik_check(context))
            elif context.scene.finger_3_right.ik_to_fk_toggle == True:
                ik_to_fk_snap(*ik_to_fk_check(context))
            elif context.scene.finger_3_right.ik_to_fk_toggle == False or context.scene.finger_3_right.fk_to_ik_toggle == False:
                return {'FINISHED'}
        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        wm = context.window_manager
        self.timer = wm.event_timer_add(utilities.DELAY, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}
    
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
    
class PanelFinger3Right(bpy.types.Panel):
    bl_idname = 'finger_3_right.mapping_panel_finger_3_right'
    bl_label = 'Finger 3 Right'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bone Snapper'
    bl_parent_id = "panel_bone_presets"
    
    def draw(self, context):
        obj = bpy.context.active_object
        col = self.layout.column()
        if obj and obj.type == 'ARMATURE':
            col.prop_search(context.scene, "finger_3_1_fk_right", obj.data, "bones")
            col.prop_search(context.scene, "finger_3_2_fk_right", obj.data, "bones")
            col.prop_search(context.scene, "finger_3_3_fk_right", obj.data, "bones")
            col.prop_search(context.scene, "finger_3_1_mch_right", obj.data, "bones")
            col.prop_search(context.scene, "finger_3_2_mch_right", obj.data, "bones")
            col.prop_search(context.scene, "finger_3_3_mch_right", obj.data, "bones")
            col.prop_search(context.scene, "finger_3_2_pole_right", obj.data, "bones")
            col.prop_search(context.scene, "finger_3_3_ik_right", obj.data, "bones")
            return
        else:
            col.label(text = "No active skeleton", icon= 'ERROR')

classes = [
    PropertiesFinger3Right,
    OperatorFinger3Right,
    PanelFinger3Right
    ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.finger_3_right = bpy.props.PointerProperty(type=PropertiesFinger3Right)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.finger_3_right