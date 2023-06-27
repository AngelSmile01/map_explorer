import glob
import json

import pyautogui as pg


from shortest_path import find_shortest_path, create_points_from_input

class Tile:
    """ The Tile class handles...
    
    """

    def __init__(self, x, y):
        """Constructor, takes a x and y position. This is the position of the time relative to the upper left corner (?)

        Args:
            x (int): Longitudinal position
            y (int): Latitudinal position
        """
        with open(f"{x}_{y}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.coordinates = data["points"]
        self.points = create_points_from_input(data["links"])

    def path(self, point1: str, point2: str):
        print(find_shortest_path(self.points, point1, point2))
        return [(point, self.coordinates[point]) for point in find_shortest_path(self.points, point1, point2)]

    def distance(self, point1: str, point2: str):
        x0, y0 = self.coordinates[point1]
        x1, y1 = self.coordinates[point2]
        return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

    def minerals_status(self):
        minerals = {"fer": [],
                    "cuivre": [],
                    "bronze": []}
        for img in glob.glob("imgs/*_full*.png"):
            boxes = find_in_screen(img, "temp.png")
            if boxes:
                for key in minerals.keys():
                    if key in img:
                        for box in boxes:
                            box = box[0]
                            minerals[key].append(((box[0][0] + box[1][0]) / 2,
                                                  (box[0][1] + box[1][1]) / 2))
        return minerals

    def travelling_time(self, point1: str, point2: str):
        return self.distance(point1, point2) / 250
