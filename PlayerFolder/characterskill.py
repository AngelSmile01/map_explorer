import json

class Skill():

    def __init__(self, skill_descriptor_string_json) -> None:
        self.skillname = skill_descriptor_string_json["skillname"]
        self.skill_range = skill_descriptor_string_json["range"]
        self.skill_cost = skill_descriptor_string_json["PA"]

class CharacterSkillset():

    def __init__(self, level, cclass):
        """Build the character skillset according to its level and class.

        Args:
            level (int): Level of the character, from 0 to 200.
            cclass (string): Class of the character, from one of the 19 available classes.
        """
        self.skills = []
        self.level = level
        
        with open("./PlayerFolder/character_skills.json") as fd_characterskills:

            data = json.loads(fd_characterskills.read())
            if cclass in data:
                for item in data[cclass]:
                    if int(item['initial_acquisition_level']) <= level:
                        self.skills.append(Skill(item))
                    
    