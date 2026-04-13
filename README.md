# Pichan Texture Updater

A Blender addon for quickly loading and reloading texture images in the Shader Editor.

## Requirements

- Blender 4.0 or higher

## Installation

1. Download the latest release (`.zip` file)
2. Open Blender
3. Go to **Edit → Preferences → Add-ons**
4. Click **Install...** and select the zip file
5. Enable the addon by checking the box next to "Pichan Texture Updater"

## Usage

1. Open your project in Blender
2. Go to the **Shader Editor**
3. Select any **Image Texture** node in your node tree
4. The addon panel will appear in the sidebar:
   - **3D Viewport**: Press **N** key → **PiChan** tab
   - **Shader Editor**: Press **N** key → **PiChan** tab
5. Click **Load Image** to open a file browser
6. Select your image file (supports .psd, .png, .jpg, .jpeg, .tga, .bmp, .exr, .tiff, .tif, .webp, .hdr)
7. Click **Reload Image** to refresh the texture if you've updated the source file

## Features

- Load images directly from file browser
- Supports multiple image formats: PSD, PNG, JPG, JPEG, TGA, BMP, EXR, TIFF, TIF, WEBP, HDR
- Reload texture to see changes without re-importing
- Available in both 3D Viewport and Shader Editor sidebars

## License

MIT License - Free to use
