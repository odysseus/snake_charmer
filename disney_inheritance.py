"""
Disney themed object inheritance examples, for my aspiring-programmer and
Disney-employee sister
"""

class Person(object):
    def __init__(self, args):
        self.first_name = args["first_name"]
        self.last_name = args["last_name"]
        self.hometown = args["hometown"]

    def greet(self):
        return "Sup, I'm {0}".format(self.first_name)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class DisneyEmployee(Person):
    def __init__(self, args):
        super(DisneyEmployee, self).__init__(args)
        self.position = args.get("position") or "CP"
        self.park = args.get("park") or "Disney"

    def state_position(self):
        return "{0}, and I am a {1} at {2}!".format(
            self.greet(), self.position, self.park)

    def greet(self):
        return "Hi! I'm {0} from {1}".format(self.first_name, self.hometown)


class Character(DisneyEmployee):
    def __init__(self, args):
        super(Character, self).__init__(args)
        self.position = "Character"
        self.park = args["park"]
        self.character_name = args["character_name"]
        self.character_hometown = args["character_hometown"]

    def greet(self):
        return "Hi! I'm {0} from {1}".format(
            self.character_name, self.character_hometown)


def disney_main():
    abbey = Person({"first_name": "Abby", "last_name": "F", "hometown": "Colorado?"})
    chelsea = DisneyEmployee({"first_name": "Kelsey",
                              "last_name": "C",
                              "hometown": "Highlands Ranch",
                              "position": "Secret Agent",
                              "park": "Disneyland"})
    princess_abbey = Character({"first_name": "Abby",
                                "last_name": "F",
                                "hometown": "Colorado",
                                "park": "DisneyWorld",
                                "character_name": "Princess Elsa",
                                "character_hometown": "Arendelle"})

    print(chelsea)
    print(princess_abbey)
    print(abbey.greet())
    print(chelsea.greet())
    print(chelsea.state_position())
    print(princess_abbey.state_position())
    print(princess_abbey.greet())