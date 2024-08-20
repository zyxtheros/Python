import pyvista as pv
from pyvista import themes
import os



class joint:
    def __init__(self, file: str, plot: pv.Plotter(), name: str, pos: tuple[float, float, float], rot: tuple[float, float, float]):
        self.file = file
        self.plot = plot
        self.name = name
        self.pos = pos # (x, y, z)
        self.rot = rot # (x angle, y angle, z angle)
        #robot arm file setup
        self.root = 'Assets/' # 'Python/python_Dash_Intro/Assets/'
        self.fileType = '.stl'
        # run the following upon instantiation
        self.mesh = self.init() # create the mesh
        self.actor = self.plot.add_mesh(self.mesh, name = self.name)   # add mesh file to the plot
        # additional helper variable..
        self.active_mesh = None

    # Automatically ran function...
    def init(self):
        mesh = pv.read(self.root+self.file+self.fileType)
        mesh = mesh.translate(self.pos)         # move mesh file before plot is added
        print("adding "+self.file+"...")

        return mesh
    def update_x(self, value: float):   # modify the x-position
        move = (value - self.pos[0], 0, 0)
        self.pos = tuple(map(lambda i, j: i + j, self.pos, move))
        self.mesh = self.mesh.translate(move)
        self.plot.add_mesh(self.mesh, name = self.name)
    def update_y(self, value: float):   # modify the y-position
        move = (0, value - self.pos[1], 0)
        self.pos = tuple(map(lambda i, j: i + j, self.pos, move))
        self.mesh = self.mesh.translate(move)
        self.plot.add_mesh(self.mesh, name = self.name)
    def update_z(self, value: float):   # modify the z-position
        move = (0, 0, value - self.pos[2])
        self.pos = tuple(map(lambda i, j: i + j, self.pos, move))
        self.mesh = self.mesh.translate(move)
        self.plot.add_mesh(self.mesh, name = self.name)
    
    def reset_colors(self):
        for a in self.plot.renderer.actors.values():
            if isinstance(a, pv.Actor):
                a.prop.color = 'white'

    # object picker functions
    @classmethod
    def picker(self, mesh):
        j1.reset_colors()
        mesh.prop.color = 'blue'
        active_mesh = mesh

def positioner_make(jnt: joint):
    # jnt.plot.add_text(jnt.name, position = "lower_right", font_size = 12, color = "black", name = "jnt_id")

    jnt.plot.add_slider_widget(callback = jnt.update_x, 
                              rng = [0, 160],
                              value = 0,
                              title='X Position',
                              pointa=(0.025, 0.95),
                              pointb=(0.31, 0.95),
                              style='modern')
    jnt.plot.add_slider_widget(callback = jnt.update_y, 
                              rng = [0, 100],
                              value = 0,
                              title='Y Position',
                              pointa=(0.35, 0.95),
                              pointb=(0.64, 0.95),
                              style='modern')
    jnt.plot.add_slider_widget(callback = jnt.update_z, 
                              rng = [0, 100],
                              value = 0,
                              title='Z Position',
                              pointa=(0.67, 0.95),
                              pointb=(0.98, 0.95),
                              style='modern')
    
plotter = pv.Plotter()
# plotter.background_color = "grey"
plotter.add_axes(line_width=5, labels_off=False)
#plotter.add_axes(box=True)
plotter.show_bounds()
pv.set_plot_theme(themes.DarkTheme())

# Add joint object to the plot
j1 = joint('P005_IntermediateArm-XYZ', plotter, "joint 1", (0, 0, 0), (0, 0, 0))
j2 = joint('P004_InputArm-XYZ', plotter, "joint 2", (0, 0, 0), (0, 0, 0))

plotter.enable_mesh_picking(joint.picker, left_clicking=True, use_actor=True, style = 'wireframe', show=False, show_message = False)
positioner_make(j1)
plotter.show()