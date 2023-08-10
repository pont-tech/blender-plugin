# Blender Add-on Template
# Contributor(s): Aaron Powell (aaron@lunadigital.tv)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.types import Panel

#
# Add additional functions here
#

class PontPanel(Panel):
    bl_label = 'pont.tech cloud'
    bl_space_type = 'PROPERTIES'
    bl_region_type= 'WINDOW'
    bl_context = 'render'

    def draw(self, context):
        row = self.layout.row()
        row.prop(context.scene, 'address')
        row1 = self.layout.row()
        row1.prop(context.scene, 'time_scale')
        row2 = self.layout.row()
        row2.prop(context.scene, 'frame_scale')

def register():
    bpy.utils.register_class(PontPanel)

def unregister():
    bpy.utils.unregister_class(PontPanel)
