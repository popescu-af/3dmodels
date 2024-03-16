import bpy
import bmesh

# Get the active mesh
obj = bpy.context.edit_object
me = obj.data


# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

bm.faces.active = None


def scaled(val):
    return int(val*1000000) / 1000

with open("~/Desktop/bottom.txt", "w") as f:
    for v in bm.verts:
        if v.select:
            # mind which points you need to write (x & y or x & z or y & z)
            f.write(f"{scaled(v.co.x)}, {scaled(v.co.y)}\n" )

