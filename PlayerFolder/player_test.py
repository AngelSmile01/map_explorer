from player import Player
# Initialization test to check that everything works properly

def test_player_name():
    p = Player("Toto", 8)
    assert p.name == "Toto"

