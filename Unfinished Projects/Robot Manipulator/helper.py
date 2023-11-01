from json import loads # String dict interpretation
import sys # import functions to kill program if errors get raised
import pyvista as pv
import dash_vtk
from dash_vtk.utils import to_mesh_state, presets

# -----------------------------------------------------------------------------
# CSS Helper Functions
# -----------------------------------------------------------------------------

# Default whitespace rules
whitespace_rules = {    # Key-value pairs of text replacements for cleaning the string
        '\n'    : '',       # Remove the carriage return
        " "     : '',       # Remove spaces created by tabs
        ';'     : '", "',   # Remove CSS line terminatros, add quote characters around params
        '--'    : '',       # Remove CSS variable prefixes
        ':'     : '": "',   # Add back in a apce between keys and values, , add quote characters around params
        ', "}'  : '}',      # Remove comma+space from last line
        '{'     : '{"'      # add leading quote character
}
# Default css theme block wrappers to search for
needle = [":root {", "}"] # Set the earch parameters for trimming
def get_css_theme(file, parse_rule = whitespace_rules, end= needle):
    f = open(file)

    haystack = f.read()
    loc = [haystack.find(end[0]), haystack.find(end[1])] # Search for the trimming locations

    # Error checking if trim boundaries were not found
    if (loc[0] == -1):   # Check the first end
        print(f"Error: block terminator '{end[0]}' does not exist in the string")
        sys.exit(0)
    elif (loc[1] == -1): # Check the second end
        print(f"Error: block terminator '{end[1]}' does not exist in the string")
        sys.exit(0)

    haystack = haystack[loc[0]+len(end[0])-1:loc[1]+1] # trim the haystack

    for key in parse_rule:  # Clean the haystack
        haystack = haystack.replace(key, parse_rule[key])  

    # Return the comprehension from string to dict
    return loads(haystack)


# -----------------------------------------------------------------------------
# 3D Model Helper Functions
# -----------------------------------------------------------------------------
IN2MM = 25.4 # inches to mm conversion, VTK and PyVista are in mm
root        = "assets/"
fileType    = ".stl"
# Predefined colors for model coloring
RGB = {"RED":       (255, 0, 0), 
       "ORANGE":    (255, 165, 0), 
       "YELLOW":    (255, 255, 0), 
       "GREEN":     (0, 255, 0), 
       "BLUE":      (0, 0, 255), 
       "VIOLET":    (165, 0, 255),
       }

#array of all models in the program
model_arr = []
class model():
    def __init__(self, fileName: str, pos = (0, 0, 0), orn = (0, 0, 0), origin = (0, 0, 0), color = (0, 0, 0), folder = root, ftype = ".stl", unitScalar = IN2MM):   
        self.fileName = folder+fileName+ftype                                   # concatenate file name components (folder, name and file type)
        self.pos = multTuple(pos, (unitScalar, unitScalar, unitScalar))         # <X, Y, Z> units default: inches
        self.orn = orn
        self.origin = multTuple(origin, (unitScalar, unitScalar, unitScalar))   # <X, Y, Z> units default: inches
        self.color = multTuple(color, (1/255, 1/255, 1/255))                    # (R, G, B) values: 0-255
        self.unitScalar = unitScalar                                            #set to 1 for mm
        model_arr.append(self)                                                  # add the model information to the collection array

# Create the geometry representation
def get_model_geometry():
    geometry = []
    for i in range(0, len(model_arr)):
        mesh = to_mesh_state(pv.read(model_arr[i].fileName))
        child = dash_vtk.GeometryRepresentation(
            children = [
               dash_vtk.Mesh(state=mesh)
            ],
            actor = {
                "orientation": model_arr[i].orn,
                "position": model_arr[i].pos,
                "origin": model_arr[i].origin,
            },
            property = {
                "color": model_arr[i].color
            },
        )
        geometry.append(child)
    return geometry


# -----------------------------------------------------------------------------
# Data Handling Helper Functions
# -----------------------------------------------------------------------------
# Multiply tuple x by tuple y
def multTuple(x: tuple, y: tuple):
    # check for length inequality
    if len(x) != len(y):
        print("Error: tuple multiplication requires params of equal length")
        sys.exit(0)

    # using zip() + generator expression
    return tuple(ele1 * ele2 for ele1, ele2 in zip(x, y))
