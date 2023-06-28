import time

from scipy.spatial.distance import cdist


from PlayerFolder.utility import find_in_screen

class Bot:
    """
          The Bot class does XXXX TBI
    """

    def __init__(self, player):
        """ Constructor of the Bot class. Takes a player in parameter.
        """
        self.player = player

    def run(self):
        """ Main execution loop of the bot
        """
        time.sleep(2)
        print("Démarrage du bot !")
        print("En recherche de minerais..")
        minerals = self.player.tile.minerals_status()
        if minerals["fer"]:
            print("Fer détecté !")
            self.player.move("floor1")
            self.player.mine(minerals["fer"])
        if minerals["bronze"]:
            print("Bronze détecté !")
            self.player.move("floor1")
            self.player.mine(minerals["bronze"])
        if minerals["cuivre"]:
            print("Cuivre détecté !")
            self.player.move("floor0")
            self.player.mine(minerals["cuivre"])
        self.player.move("floor2")
        self.player.move("to_9_-19_BT")
        # self.player.move("cave")
        # self.player.patrol("floor0", "floor1")


