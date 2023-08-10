import bpy
from bpy.types import Scene

from bpy.props import IntProperty
from bpy.props import StringProperty

def register():
    Scene.address = StringProperty(default="http://localhost:5000")
    Scene.time_scale = IntProperty(default=1)
    Scene.frame_scale = IntProperty(default=2)

def unregister():
    del Scene.address 
    del Scene.time_scale 
    del Scene.frame_scale 

