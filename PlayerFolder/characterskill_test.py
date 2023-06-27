from characterskill import CharacterSkillset

def test_character_skill_set_empty_with_wrong_level():
    skillset = CharacterSkillset(-10, "sram")
    assert len(skillset.skills) == 0

def test_unknown_class_character_empty():
    skillset = CharacterSkillset(10, "ThisClassDoesntExist")
    assert len(skillset.skills) == 0

def test_sram_level_one_should_contain_3_skills():
    skillset = CharacterSkillset(1, "sram")
    assert len(skillset.skills) == 3