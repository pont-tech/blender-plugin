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

bl_info = {
        "name": "pont.tech cloud plugin",
        "description": "Postprocess cloud upscaling and interpolation",
        "author": "Nikita Krutoy",
        "version": (0, 0, 1),
        "blender": (3, 2, 2),
        "location": "Properties > Render > pont.tech cloud",
        "warning": "", # used for warning icon and text in add-ons panel
        "support": "COMMUNITY",
        "category": "Render"
        }

import bpy

#
# Add additional functions here
#

def register():
    from . import properties
    from . import ui
    from . import handlers

    properties.register()
    ui.register()
    handlers.register()

def unregister():
    from . import properties
    from . import ui
    from . import handlers

    properties.unregister()
    ui.unregister()
    handlers.register()


if __name__ == '__main__':
    register()
