from utility import match_image
from bot import Bot
from player import Player


def test_find_piou_in_map():
    matches = match_image(
        "./PlayerFolder/TestSamples/piou.png",
        "./PlayerFolder/TestSamples/detect_piou.png",
        overlap_threshold=0.5,
        threshold=0.97,
    )
    assert len(matches) > 0


def test_movements_are_not_linear():
    player = Player("Bibi", 30, "sram")
    Bot(player)
    assert 2 < 1
