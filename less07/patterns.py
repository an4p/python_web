# files shared from my missed lesson
#Gof
class Building:
    def make_basement(self, basement):
        pass
    def make_walls(self, walls):
        pass
    def make_roof(self, roof):
        pass

class Skyscriber(Building):
    def __init__(self):
        self.basement = None
        self.walls = None
        self.roof = None

    def make_basement(self, basement):
        self.basement = basement
    def make_walls(self, walls):
        self.walls = walls
    def make_roof(self, roof):
        self.roof = roof

class Cottage(Building):
    def __init__(self):
        self.basement = None
        self.walls = None
        self.roof = None

    def make_basement(self, basement):
        self.basement = basement
        print("Basement")

    def make_walls(self, walls):
        self.walls = walls
        print("Walls")

    def make_roof(self, roof):
        self.roof = roof
        print("Roof")

class Foreman:
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.build_basement()
        self.builder.build_walls()
        self.builder.build_roof()

class Builder:
    def __init__(self):
        self.building = None
    def get_building(self):
        return self.building

    def build_basement(self):
        pass

    def build_walls(self):
        pass

    def build_roof(self):
        pass

class Skyscriber_builder(Builder):
    def __init__(self):
        Builder.__init__(self)
        self.building = Skyscriber()

    def build_basement(self):
        self.building.make_basement("Basement")

    def build_walls(self):
        self.building.make_walls("Walls")

    def build_roof(self):
        self.building.make_roof("Roof")


class Cottage_builder(Builder):
    def __init__(self):
        Builder.__init__(self)
        self.building = Cottage()

    def build_basement(self):
        self.building.make_basement("Basement")

    def build_walls(self):
        self.building.make_walls("Walls")

    def build_roof(self):
        self.building.make_roof("Roof")

def main():
    cottage_builder = Cottage_builder()
    foreman = Foreman(cottage_builder)
    foreman.build()
    cottage = cottage_builder.get_building()

main()