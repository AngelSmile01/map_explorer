from tile import Tile

class Player:
    """ The Player class contains all the information about the Player (us)
    """
    def __init__(self, name, level):
        """_summary_

        Args:
            name (string): Name of our character.
            level (int): Level of our character.
        """

        self.name = name
        self.level = level
        self.speed = 100
        self.tile = Tile(10, -19)
        self.position = "floor1"

    def move(self, point):
        """_summary_

        Args:
            point (_type_): _description_
        """
        path = self.tile.path(self.position, point)
        print("Joueur en direction de :", point)
        for path_info in path:
            point_name, point_coordinates = path_info
            if self.position == point_name:
                continue
            x, y = point_coordinates
            print(f"\t-> {point_name} {point_coordinates}")
            pg.moveTo(x, y)
            pg.click()
            time.sleep(self.tile.travelling_time(self.position, point_name))
            self.position = point_name
        print()

    def patrol(self, point1, point2):
        self.move(point1)
        self.move(point2)

    def mine(self, minerals_coordinates):
        for mineral_coordinates in minerals_coordinates:
            print(f"Minage de", mineral_coordinates)
            # A None mistake here
            x, y = mineral_coordinates
            pg.moveTo(x, y)
            pg.click()
            time.sleep(3)
        self.move(self.position)
