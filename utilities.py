import bpy

DELAY = 0.01

def get_bones_with_check(context, bone_names):
    obj = context.active_object
    if not obj or obj.type != 'ARMATURE':
        return None
    bones = []
    for name in bone_names:
        bone = obj.pose.bones.get(name)
        if not bone:
            return None 
        bones.append(bone)
    return bones

def any_snapping_possible(*bone_sets):
    return any(all(bone_set) for bone_set in bone_sets)

PROPS = [
    ('arm_1_fk_left', bpy.props.StringProperty(name='FK Upper')),
    ('arm_2_fk_left', bpy.props.StringProperty(name='FK Lower')),
    ('arm_3_fk_left', bpy.props.StringProperty(name='FK End')),
    ('arm_1_mch_left', bpy.props.StringProperty(name='MCH Upper')),
    ('arm_2_mch_left', bpy.props.StringProperty(name='MCH Lower')),
    ('arm_3_mch_left', bpy.props.StringProperty(name='MCH End')),
    ('arm_2_pole_left', bpy.props.StringProperty(name='IK Pole')),
    ('arm_3_ik_left', bpy.props.StringProperty(name='IK Target')),

    ('arm_1_fk_right', bpy.props.StringProperty(name='FK Upper')),
    ('arm_2_fk_right', bpy.props.StringProperty(name='FK Lower')),
    ('arm_3_fk_right', bpy.props.StringProperty(name='FK End')),
    ('arm_1_mch_right', bpy.props.StringProperty(name='IK Upper')),
    ('arm_2_mch_right', bpy.props.StringProperty(name='IK Lower')),
    ('arm_3_mch_right', bpy.props.StringProperty(name='IK End')),
    ('arm_2_pole_right', bpy.props.StringProperty(name='IK Pole')),
    ('arm_3_ik_right', bpy.props.StringProperty(name='IK Target')),

    ('leg_1_fk_left', bpy.props.StringProperty(name='FK Upper')),
    ('leg_2_fk_left', bpy.props.StringProperty(name='FK Lower')),
    ('leg_3_fk_left', bpy.props.StringProperty(name='FK End')),
    ('leg_1_mch_left', bpy.props.StringProperty(name='MCH Upper')),
    ('leg_2_mch_left', bpy.props.StringProperty(name='MCH Lower')),
    ('leg_3_mch_left', bpy.props.StringProperty(name='MCH End')),
    ('leg_2_pole_left', bpy.props.StringProperty(name='IK Pole')),
    ('leg_3_ik_left', bpy.props.StringProperty(name='IK Target')),

    ('leg_1_fk_right', bpy.props.StringProperty(name='FK Upper')),
    ('leg_2_fk_right', bpy.props.StringProperty(name='FK Lower')),
    ('leg_3_fk_right', bpy.props.StringProperty(name='FK End')),
    ('leg_1_mch_right', bpy.props.StringProperty(name='IK Upper')),
    ('leg_2_mch_right', bpy.props.StringProperty(name='IK Lower')),
    ('leg_3_mch_right', bpy.props.StringProperty(name='IK End')),
    ('leg_2_pole_right', bpy.props.StringProperty(name='IK Pole')),
    ('leg_3_ik_right', bpy.props.StringProperty(name='IK Target')),

    ('finger_1_1_fk_left', bpy.props.StringProperty(name='FK Upper')),
    ('finger_1_2_fk_left', bpy.props.StringProperty(name='FK Lower')),
    ('finger_1_3_fk_left', bpy.props.StringProperty(name='FK End')),
    ('finger_1_1_mch_left', bpy.props.StringProperty(name='IK Upper')),
    ('finger_1_2_mch_left', bpy.props.StringProperty(name='IK Lower')),
    ('finger_1_3_mch_left', bpy.props.StringProperty(name='IK End')),
    ('finger_1_2_pole_left', bpy.props.StringProperty(name='IK Pole')),
    ('finger_1_3_ik_left', bpy.props.StringProperty(name='IK Target')),

    ('finger_2_1_fk_left', bpy.props.StringProperty(name='FK Upper')),
    ('finger_2_2_fk_left', bpy.props.StringProperty(name='FK Lower')),
    ('finger_2_3_fk_left', bpy.props.StringProperty(name='FK End')),
    ('finger_2_1_mch_left', bpy.props.StringProperty(name='IK Upper')),
    ('finger_2_2_mch_left', bpy.props.StringProperty(name='IK Lower')),
    ('finger_2_3_mch_left', bpy.props.StringProperty(name='IK End')),
    ('finger_2_2_pole_left', bpy.props.StringProperty(name='IK Pole')),
    ('finger_2_3_ik_left', bpy.props.StringProperty(name='IK Target')),

    ('finger_3_1_fk_left', bpy.props.StringProperty(name='FK Upper')),
    ('finger_3_2_fk_left', bpy.props.StringProperty(name='FK Lower')),
    ('finger_3_3_fk_left', bpy.props.StringProperty(name='FK End')),
    ('finger_3_1_mch_left', bpy.props.StringProperty(name='IK Upper')),
    ('finger_3_2_mch_left', bpy.props.StringProperty(name='IK Lower')),
    ('finger_3_3_mch_left', bpy.props.StringProperty(name='IK End')),
    ('finger_3_2_pole_left', bpy.props.StringProperty(name='IK Pole')),
    ('finger_3_3_ik_left', bpy.props.StringProperty(name='IK Target')),

    ('finger_4_1_fk_left', bpy.props.StringProperty(name='FK Upper')),
    ('finger_4_2_fk_left', bpy.props.StringProperty(name='FK Lower')),
    ('finger_4_3_fk_left', bpy.props.StringProperty(name='FK End')),
    ('finger_4_1_mch_left', bpy.props.StringProperty(name='IK Upper')),
    ('finger_4_2_mch_left', bpy.props.StringProperty(name='IK Lower')),
    ('finger_4_3_mch_left', bpy.props.StringProperty(name='IK End')),
    ('finger_4_2_pole_left', bpy.props.StringProperty(name='IK Pole')),
    ('finger_4_3_ik_left', bpy.props.StringProperty(name='IK Target')),

    ('finger_5_1_fk_left', bpy.props.StringProperty(name='FK Upper')),
    ('finger_5_2_fk_left', bpy.props.StringProperty(name='FK Lower')),
    ('finger_5_3_fk_left', bpy.props.StringProperty(name='FK End')),
    ('finger_5_1_mch_left', bpy.props.StringProperty(name='IK Upper')),
    ('finger_5_2_mch_left', bpy.props.StringProperty(name='IK Lower')),
    ('finger_5_3_mch_left', bpy.props.StringProperty(name='IK End')),
    ('finger_5_2_pole_left', bpy.props.StringProperty(name='IK Pole')),
    ('finger_5_3_ik_left', bpy.props.StringProperty(name='IK Target')),

    ('finger_1_1_fk_right', bpy.props.StringProperty(name='FK Upper')),
    ('finger_1_2_fk_right', bpy.props.StringProperty(name='FK Lower')),
    ('finger_1_3_fk_right', bpy.props.StringProperty(name='FK End')),
    ('finger_1_1_mch_right', bpy.props.StringProperty(name='IK Upper')),
    ('finger_1_2_mch_right', bpy.props.StringProperty(name='IK Lower')),
    ('finger_1_3_mch_right', bpy.props.StringProperty(name='IK End')),
    ('finger_1_2_pole_right', bpy.props.StringProperty(name='IK Pole')),
    ('finger_1_3_ik_right', bpy.props.StringProperty(name='IK Target')),

    ('finger_2_1_fk_right', bpy.props.StringProperty(name='FK Upper')),
    ('finger_2_2_fk_right', bpy.props.StringProperty(name='FK Lower')),
    ('finger_2_3_fk_right', bpy.props.StringProperty(name='FK End')),
    ('finger_2_1_mch_right', bpy.props.StringProperty(name='IK Upper')),
    ('finger_2_2_mch_right', bpy.props.StringProperty(name='IK Lower')),
    ('finger_2_3_mch_right', bpy.props.StringProperty(name='IK End')),
    ('finger_2_2_pole_right', bpy.props.StringProperty(name='IK Pole')),
    ('finger_2_3_ik_right', bpy.props.StringProperty(name='IK Target')),

    ('finger_3_1_fk_right', bpy.props.StringProperty(name='FK Upper')),
    ('finger_3_2_fk_right', bpy.props.StringProperty(name='FK Lower')),
    ('finger_3_3_fk_right', bpy.props.StringProperty(name='FK End')),
    ('finger_3_1_mch_right', bpy.props.StringProperty(name='IK Upper')),
    ('finger_3_2_mch_right', bpy.props.StringProperty(name='IK Lower')),
    ('finger_3_3_mch_right', bpy.props.StringProperty(name='IK End')),
    ('finger_3_2_pole_right', bpy.props.StringProperty(name='IK Pole')),
    ('finger_3_3_ik_right', bpy.props.StringProperty(name='IK Target')),

    ('finger_4_1_fk_right', bpy.props.StringProperty(name='FK Upper')),
    ('finger_4_2_fk_right', bpy.props.StringProperty(name='FK Lower')),
    ('finger_4_3_fk_right', bpy.props.StringProperty(name='FK End')),
    ('finger_4_1_mch_right', bpy.props.StringProperty(name='IK Upper')),
    ('finger_4_2_mch_right', bpy.props.StringProperty(name='IK Lower')),
    ('finger_4_3_mch_right', bpy.props.StringProperty(name='IK End')),
    ('finger_4_2_pole_right', bpy.props.StringProperty(name='IK Pole')),
    ('finger_4_3_ik_right', bpy.props.StringProperty(name='IK Target')),

    ('finger_5_1_fk_right', bpy.props.StringProperty(name='FK Upper')),
    ('finger_5_2_fk_right', bpy.props.StringProperty(name='FK Lower')),
    ('finger_5_3_fk_right', bpy.props.StringProperty(name='FK End')),
    ('finger_5_1_mch_right', bpy.props.StringProperty(name='IK Upper')),
    ('finger_5_2_mch_right', bpy.props.StringProperty(name='IK Lower')),
    ('finger_5_3_mch_right', bpy.props.StringProperty(name='IK End')),
    ('finger_5_2_pole_right', bpy.props.StringProperty(name='IK Pole')),
    ('finger_5_3_ik_right', bpy.props.StringProperty(name='IK Target'))
]

def register():
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)

def unregister():
    for (prop_name, _) in PROPS:
        delattr(bpy.types.Scene, prop_name)