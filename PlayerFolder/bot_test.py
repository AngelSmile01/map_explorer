from utility import match_image

def test_find_piou_in_map():
    matches = match_image("./PlayerFolder/TestSamples/piou.png", "./PlayerFolder/TestSamples/detect_piou.png", overlap_threshold=0.5, threshold=0.97)
    print(matches)
    assert len(matches) > 0