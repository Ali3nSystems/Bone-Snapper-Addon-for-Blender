import bpy
from . import operators

from . import arm_left
from . import arm_right

from . import leg_left
from . import leg_right

from . import finger_1_left
from . import finger_2_left
from . import finger_3_left
from . import finger_4_left
from . import finger_5_left

from . import finger_1_right
from . import finger_2_right
from . import finger_3_right
from . import finger_4_right
from . import finger_5_right

class PanelSnappingOperations(bpy.types.Panel):
    bl_idname = 'panel_snapping_operations'
    bl_label = 'Snapping Operations'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bone Snapper'
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        obj = bpy.context.active_object
        if obj and obj.type == 'ARMATURE':
            arm_left.draw_ui_arm_left(self, context, arm_left.ik_to_fk_bone_objects(), arm_left.fk_to_ik_bone_objects())
            arm_right.draw_ui_arm_right(self, context, arm_right.ik_to_fk_bone_objects(), arm_right.fk_to_ik_bone_objects())

            leg_left.draw_ui_leg_left(self, context, leg_left.ik_to_fk_bone_objects(), leg_left.fk_to_ik_bone_objects())
            leg_right.draw_ui_leg_right(self, context, leg_right.ik_to_fk_bone_objects(), leg_right.fk_to_ik_bone_objects())
            
            finger_1_left.draw_ui_finger_1_left(self, context, finger_1_left.ik_to_fk_bone_objects(), finger_1_left.fk_to_ik_bone_objects())
            finger_2_left.draw_ui_finger_2_left(self, context, finger_2_left.ik_to_fk_bone_objects(), finger_2_left.fk_to_ik_bone_objects())
            finger_3_left.draw_ui_finger_3_left(self, context, finger_3_left.ik_to_fk_bone_objects(), finger_3_left.fk_to_ik_bone_objects())
            finger_4_left.draw_ui_finger_4_left(self, context, finger_4_left.ik_to_fk_bone_objects(), finger_4_left.fk_to_ik_bone_objects())
            finger_5_left.draw_ui_finger_5_left(self, context, finger_5_left.ik_to_fk_bone_objects(), finger_5_left.fk_to_ik_bone_objects())
            
            finger_1_right.draw_ui_finger_1_right(self, context, finger_1_right.ik_to_fk_bone_objects(), finger_1_right.fk_to_ik_bone_objects())
            finger_2_right.draw_ui_finger_2_right(self, context, finger_2_right.ik_to_fk_bone_objects(), finger_2_right.fk_to_ik_bone_objects())
            finger_3_right.draw_ui_finger_3_right(self, context, finger_3_right.ik_to_fk_bone_objects(), finger_3_right.fk_to_ik_bone_objects())
            finger_4_right.draw_ui_finger_4_right(self, context, finger_4_right.ik_to_fk_bone_objects(), finger_4_right.fk_to_ik_bone_objects())
            finger_5_right.draw_ui_finger_5_right(self, context, finger_5_right.ik_to_fk_bone_objects(), finger_5_right.fk_to_ik_bone_objects())
            
        else:
            col.label(text ="No active armature", icon='ERROR')

class PanelBonePresets(bpy.types.Panel):
    bl_idname = 'panel_bone_presets'
    bl_label = 'Bone Presets'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bone Snapper'
    
    def draw_header_preset(self, _context):
        operators.PanelPreset.draw_panel_header(self.layout)
    
    def draw(self, context):
        col = self.layout.column()
        col.operator("bone_snapper.operator_open_preset_directory", icon="FILEBROWSER")

classes = [
    PanelSnappingOperations,
    PanelBonePresets
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)