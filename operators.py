import bpy
from bl_operators.presets import AddPresetBase
from bl_ui.utils import PresetPanel

class OperatorOpenPresetDirectory(bpy.types.Operator):
    bl_idname = "bone_snapper.operator_open_preset_directory"
    bl_label = "Open Preset Directory"

    def execute(self, context):
        preset_paths = bpy.utils.preset_paths("BoneSnapper") 
        if preset_paths:
            preset_path = preset_paths[0]
            bpy.ops.wm.path_open(filepath=preset_path)
        else:
            self.report({'ERROR'}, "Preset directory not found")
        return {'FINISHED'}

class MenuPreset(bpy.types.Menu): 
    bl_label = 'Preset Menu' 
    bl_idname = 'menu_preset'
    preset_subdir = 'BoneSnapper'
    preset_operator = 'script.execute_preset'
    draw = bpy.types.Menu.draw_preset

class PanelPreset(PresetPanel, bpy.types.Panel):
    bl_label = 'Preset Panel'
    preset_subdir = 'BoneSnapper'
    preset_operator = 'script.execute_preset'
    preset_add_operator = 'bone_snapper.preset_add'

class OperatorAddPreset(AddPresetBase, bpy.types.Operator):
    bl_idname = 'bone_snapper.preset_add'
    bl_label = 'Add A Preset'
    preset_menu = 'menu_preset'
    preset_defines = [
                        'obj = bpy.context.object',
                        'scene = bpy.context.scene'
                     ]
    preset_values = [
                        'scene.arm_1_fk_left',
                        'scene.arm_2_fk_left',
                        'scene.arm_3_fk_left',
                        'scene.arm_1_mch_left',
                        'scene.arm_2_mch_left',
                        'scene.arm_3_mch_left',
                        'scene.arm_2_pole_left',
                        'scene.arm_3_ik_left',

                        'scene.arm_1_fk_right',
                        'scene.arm_2_fk_right',
                        'scene.arm_3_fk_right',
                        'scene.arm_1_mch_right',
                        'scene.arm_2_mch_right',
                        'scene.arm_3_mch_right',
                        'scene.arm_2_pole_right',
                        'scene.arm_3_ik_right',

                        'scene.leg_1_fk_left',
                        'scene.leg_2_fk_left',
                        'scene.leg_3_fk_left',
                        'scene.leg_1_mch_left',
                        'scene.leg_2_mch_left',
                        'scene.leg_3_mch_left',
                        'scene.leg_2_pole_left',
                        'scene.leg_3_ik_left',

                        'scene.leg_1_fk_right',
                        'scene.leg_2_fk_right',
                        'scene.leg_3_fk_right',
                        'scene.leg_1_mch_right',
                        'scene.leg_2_mch_right',
                        'scene.leg_3_mch_right',
                        'scene.leg_2_pole_right',
                        'scene.leg_3_ik_right',

                        'scene.finger_1_1_fk_left', 
                        'scene.finger_1_2_fk_left', 
                        'scene.finger_1_3_fk_left', 
                        'scene.finger_1_1_mch_left', 
                        'scene.finger_1_2_mch_left', 
                        'scene.finger_1_3_mch_left', 
                        'scene.finger_1_2_pole_left', 
                        'scene.finger_1_3_ik_left',

                        'scene.finger_2_1_fk_left', 
                        'scene.finger_2_2_fk_left', 
                        'scene.finger_2_3_fk_left', 
                        'scene.finger_2_1_mch_left', 
                        'scene.finger_2_2_mch_left', 
                        'scene.finger_2_3_mch_left', 
                        'scene.finger_2_2_pole_left', 
                        'scene.finger_2_3_ik_left',

                        'scene.finger_3_1_fk_left', 
                        'scene.finger_3_2_fk_left', 
                        'scene.finger_3_3_fk_left', 
                        'scene.finger_3_1_mch_left', 
                        'scene.finger_3_2_mch_left', 
                        'scene.finger_3_3_mch_left', 
                        'scene.finger_3_2_pole_left', 
                        'scene.finger_3_3_ik_left',

                        'scene.finger_4_1_fk_left', 
                        'scene.finger_4_2_fk_left', 
                        'scene.finger_4_3_fk_left', 
                        'scene.finger_4_1_mch_left', 
                        'scene.finger_4_2_mch_left', 
                        'scene.finger_4_3_mch_left', 
                        'scene.finger_4_2_pole_left', 
                        'scene.finger_4_3_ik_left',

                        'scene.finger_5_1_fk_left', 
                        'scene.finger_5_2_fk_left', 
                        'scene.finger_5_3_fk_left', 
                        'scene.finger_5_1_mch_left', 
                        'scene.finger_5_2_mch_left', 
                        'scene.finger_5_3_mch_left', 
                        'scene.finger_5_2_pole_left', 
                        'scene.finger_5_3_ik_left',

                        'scene.finger_1_1_fk_right', 
                        'scene.finger_1_2_fk_right', 
                        'scene.finger_1_3_fk_right', 
                        'scene.finger_1_1_mch_right', 
                        'scene.finger_1_2_mch_right', 
                        'scene.finger_1_3_mch_right', 
                        'scene.finger_1_2_pole_right', 
                        'scene.finger_1_3_ik_right',

                        'scene.finger_2_1_fk_right', 
                        'scene.finger_2_2_fk_right', 
                        'scene.finger_2_3_fk_right', 
                        'scene.finger_2_1_mch_right', 
                        'scene.finger_2_2_mch_right', 
                        'scene.finger_2_3_mch_right', 
                        'scene.finger_2_2_pole_right', 
                        'scene.finger_2_3_ik_right',

                        'scene.finger_3_1_fk_right', 
                        'scene.finger_3_2_fk_right', 
                        'scene.finger_3_3_fk_right', 
                        'scene.finger_3_1_mch_right', 
                        'scene.finger_3_2_mch_right', 
                        'scene.finger_3_3_mch_right', 
                        'scene.finger_3_2_pole_right', 
                        'scene.finger_3_3_ik_right',

                        'scene.finger_4_1_fk_right', 
                        'scene.finger_4_2_fk_right', 
                        'scene.finger_4_3_fk_right', 
                        'scene.finger_4_1_mch_right', 
                        'scene.finger_4_2_mch_right', 
                        'scene.finger_4_3_mch_right', 
                        'scene.finger_4_2_pole_right', 
                        'scene.finger_4_3_ik_right',

                        'scene.finger_5_1_fk_right', 
                        'scene.finger_5_2_fk_right', 
                        'scene.finger_5_3_fk_right', 
                        'scene.finger_5_1_mch_right', 
                        'scene.finger_5_2_mch_right', 
                        'scene.finger_5_3_mch_right', 
                        'scene.finger_5_2_pole_right', 
                        'scene.finger_5_3_ik_right'
                    ]
    preset_subdir = 'BoneSnapper'

classes = [
    OperatorOpenPresetDirectory,
    MenuPreset,
    PanelPreset,
    OperatorAddPreset
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)