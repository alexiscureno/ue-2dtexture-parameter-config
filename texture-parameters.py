import unreal

editor_asset_lib = unreal.EditorAssetLibrary()
string_lib = unreal.StringLibrary()

source_dir = "/Game/"
include_subfolders = True
set_textures = 0

asset = editor_asset_lib.list_assets(source_dir, recursive=include_subfolders)
color_patterns = ["_ORM", "_OcclusionRoughnessMetallic", "_Metallic", "_Roughness", "_Mask", "_Albedo", "_BaseColor", "_Diffuse", "_Transparency"]

for asset in asset:
    for pattern in color_patterns:
        if string_lib.contains(asset, pattern):
            asset_obj = editor_asset_lib.load_asset(asset)
            asset_obj.set_editor_property("sRGB", False)
            asset_obj.set_editor_property("CompressionSettings", unreal.TextureCompressionSettings.TC_MASKS)

            unreal.log("Settings TC_Masks and turning off sRGB for asset {}".format(asset))
            set_textures += 1
            break
unreal.log("Linear color for matching textures set for {}".format(set_textures))
