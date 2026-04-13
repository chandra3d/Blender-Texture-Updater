import bpy
from .operators import get_active_image_texture_node


# ─────────────────────────────────────────────
#  Panel A — 3D Viewport sidebar  (N key)
# ─────────────────────────────────────────────
class TEXTURE_UPDATER_PT_view3d(bpy.types.Panel):
    bl_label = "PiChan Texture"
    bl_idname = "TEXTURE_UPDATER_PT_view3d"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PiChan"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def draw(self, context):
        layout = self.layout
        obj = context.active_object
        node = get_active_image_texture_node(context)

        col = layout.column(align=True)
        col.label(text=f"Object: {obj.name}", icon="OBJECT_DATA")
        col.separator()

        if node is None:
            col.label(text="Go to Shader Editor,", icon="INFO")
            col.label(text="select Image Texture node")
            col.label(text="then click below:")
            col.separator()
            row = col.row()
            row.enabled = False
            row.operator(
                "texture_updater.load_texture",
                text="Load Image  (.psd .png .jpg …)",
                icon="FILE_FOLDER",
            )
        else:
            col.label(text=f"Node: {node.name}", icon="NODE_TEXTURE")
            if node.image:
                col.label(text=node.image.name, icon="IMAGE_DATA")
            else:
                col.label(text="No image loaded", icon="QUESTION")
            col.separator()
            col.operator(
                "texture_updater.load_texture",
                text="Load Image  (.psd .png .jpg …)",
                icon="FILE_FOLDER",
            )
            col.operator(
                "texture_updater.reload_texture",
                text="Reload Image",
                icon="FILE_REFRESH",
            )


# ─────────────────────────────────────────────
#  Panel B — Shader Editor sidebar  (N key)
# ─────────────────────────────────────────────
class TEXTURE_UPDATER_PT_shader(bpy.types.Panel):
    bl_label = "PiChan Texture"
    bl_idname = "TEXTURE_UPDATER_PT_shader"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "PiChan"

    @classmethod
    def poll(cls, context):
        sd = context.space_data
        return (
            sd is not None
            and sd.type == 'NODE_EDITOR'
            and sd.tree_type == 'ShaderNodeTree'
        )

    def draw(self, context):
        layout = self.layout
        node = get_active_image_texture_node(context)

        if node is None:
            col = layout.column(align=True)
            col.label(text="Select an Image Texture", icon="INFO")
            col.label(text="node in the shader tree")
            col.separator()
            row = col.row()
            row.enabled = False
            row.operator(
                "texture_updater.load_texture",
                text="Load Image  (.psd .png .jpg …)",
                icon="FILE_FOLDER",
            )
        else:
            col = layout.column(align=True)
            col.label(text=f"Node: {node.name}", icon="NODE_TEXTURE")
            if node.image:
                col.label(text=node.image.name, icon="IMAGE_DATA")
            else:
                col.label(text="No image loaded", icon="QUESTION")
            col.separator()
            col.operator(
                "texture_updater.load_texture",
                text="Load Image  (.psd .png .jpg …)",
                icon="FILE_FOLDER",
            )
            col.operator(
                "texture_updater.reload_texture",
                text="Reload Image",
                icon="FILE_REFRESH",
            )


def register():
    bpy.utils.register_class(TEXTURE_UPDATER_PT_view3d)
    bpy.utils.register_class(TEXTURE_UPDATER_PT_shader)


def unregister():
    bpy.utils.unregister_class(TEXTURE_UPDATER_PT_shader)
    bpy.utils.unregister_class(TEXTURE_UPDATER_PT_view3d)
