import bpy
import os


def get_active_image_texture_node(context):
    """Return the active Image Texture node in the shader node tree, or None."""
    obj = context.active_object
    if obj is None:
        return None
    mat = obj.active_material
    if mat is None or not mat.use_nodes:
        return None
    node = mat.node_tree.nodes.active
    if node and node.type == 'TEX_IMAGE':
        return node
    return None


class TEXTURE_UPDATER_OT_load_texture(bpy.types.Operator):
    """Open a file browser and load the selected image into the active Image Texture node"""
    bl_idname = "texture_updater.load_texture"
    bl_label = "Load Image"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(
        subtype='FILE_PATH',
        options={'HIDDEN', 'SKIP_SAVE'},
    )
    filter_folder: bpy.props.BoolProperty(
        default=True,
        options={'HIDDEN', 'SKIP_SAVE'},
    )
    filter_glob: bpy.props.StringProperty(
        # includes PSD — Blender reads it via OpenImageIO
        default="*.png;*.jpg;*.jpeg;*.tga;*.bmp;*.exr;*.tiff;*.tif;*.webp;*.hdr;*.psd",
        options={'HIDDEN'},
    )

    @classmethod
    def poll(cls, context):
        return get_active_image_texture_node(context) is not None

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        node = get_active_image_texture_node(context)
        if node is None:
            self.report({'WARNING'}, "No active Image Texture node found")
            return {'CANCELLED'}

        filepath = bpy.path.abspath(self.filepath)
        if not os.path.isfile(filepath):
            self.report({'ERROR'}, f"File not found: {filepath}")
            return {'CANCELLED'}

        # Load (or reuse) image datablock, then assign to node
        img = bpy.data.images.load(filepath, check_existing=True)
        node.image = img

        self.report({'INFO'}, f"Loaded: {os.path.basename(filepath)}")
        return {'FINISHED'}


class TEXTURE_UPDATER_OT_reload_texture(bpy.types.Operator):
    """Reload the image in the active Image Texture node"""
    bl_idname = "texture_updater.reload_texture"
    bl_label = "Reload Image"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        node = get_active_image_texture_node(context)
        return node is not None and node.image is not None

    def execute(self, context):
        node = get_active_image_texture_node(context)
        if node and node.image:
            node.image.reload()
            self.report({'INFO'}, f"Reloaded: {node.image.name}")
            return {'FINISHED'}
        return {'CANCELLED'}


def register():
    bpy.utils.register_class(TEXTURE_UPDATER_OT_load_texture)
    bpy.utils.register_class(TEXTURE_UPDATER_OT_reload_texture)


def unregister():
    bpy.utils.unregister_class(TEXTURE_UPDATER_OT_reload_texture)
    bpy.utils.unregister_class(TEXTURE_UPDATER_OT_load_texture)

