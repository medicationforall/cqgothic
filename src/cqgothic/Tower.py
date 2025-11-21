from cadqueryhelper import Base
import cadquery as cq
from . import Bunker

class Tower(Base):
    def __init__(self):
        super().__init__()
        self.stories = 3
        self.length = 150
        self.width = 150
        self.story_height = 75

        self.panel_width = 5
        self.panel_length = 30
        self.skip_windows=[]
        self.ladder_panels = [0]

        self.render_ladders = False
        self.render_panel_details = False
        self.render_floor_tiles = False
        self.render_pips=True
        self.render_magnets=True

        self.floors_bp = None
        self.floors = None

    def make_floor(self, index):
        bp = Bunker()
        bp.length = self.length
        bp.width = self.width
        bp.height = self.story_height
        bp.panel_width = self.panel_width
        bp.panel_length = self.panel_length
        bp.skip_windows = self.skip_windows

        bp.render_ladders = self.render_ladders
        bp.ladder_panels = self.ladder_panels
        bp.render_panel_details = self.render_panel_details
        bp.render_pips = self.render_pips
        bp.render_magnets = self.render_magnets

        bp.render_roof = False
        if index == 0:
            bp.render_doors = True
        else:
            bp.render_doors = False

        bp.render_floor_tiles = self.render_floor_tiles
        bp.make()
        return bp

    def make(self):
        super().make()
        self.floors_bp = []
        for i in range(self.stories):
            self.floors_bp.append(self.make_floor(i))

    def build(self):
        super().build()
        scene = cq.Workplane("XY")
        self.floors = []
        for i, floor_bp in enumerate(self.floors_bp):
            floor = floor_bp.build()
            self.floors.append(floor)
            scene.add(floor.translate((0,0,i*self.story_height)))

        return scene
