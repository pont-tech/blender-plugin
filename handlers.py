import bpy
import requests

def post_render_handler(scene):
    # Get the render result
    result = bpy.data.images['Render Result']
    input_path = 'C:/tmp/image.png'
    output_path = bpy.context.scene.render.filepath
    
    # Save the render result
    result.save_render(input_path)

    with open(input_path, 'rb') as f:
        image_data = f.read()

    # Send the image to the Flask server
    response = requests.post(scene.address, files={'image': image_data})

    # Save the processed image received from the Flask server
    frame = bpy.context.scene.frame_current
    with open(f'{output_path}/{frame}.png', 'wb') as f:
        f.write(response.content)
        
    image = bpy.data.images.load(f'{output_path}/{frame}.png')

    # Update the current project's screen
    #bpy.context.window.screen = bpy.data.screens['Image Editor']
    bpy.context.area.ui_type = 'IMAGE_EDITOR'

    # Set the image as the active image in the image editor
    bpy.context.area.spaces.active.image = image
    print("Render finished!")

def register():
    bpy.app.handlers.render_post.append(post_render_handler)

def unregister():
    bpy.app.handlers.render_post.remove(post_render_handler)
