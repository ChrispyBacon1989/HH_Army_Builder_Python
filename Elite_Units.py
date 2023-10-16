class CataphractiiTerminatorSquad:
    def __init__(self, unit_type, name, unit_size, base_points, additional_points):
        self.unit_type = unit_type
        self.name = name
        self.unit_size = unit_size
        self.base_points = base_points
        self.additional_points = additional_points
        pass


class CataphractiiTerminatorTacticalSquad(CataphractiiTerminatorSquad):
    def __init__(self, unit_type, name, unit_size, base_points, additional_points):
        pass


class CataphractiiTerminatorAssaultSquad(CataphractiiTerminatorSquad):
    def __init__(self, unit_type, name, unit_size, base_points, additional_points):
        pass


class TartarosTerminatorSquad:
    def __init__(self, unit_type, name, unit_size, base_points, additional_points):
        self.unit_type = unit_type
        self.name = name
        self.unit_size = unit_size
        self.base_points = base_points
        self.additional_points = additional_points
        pass


class TartarosTerminatorTacticalSquad(TartarosTerminatorSquad):
    def __init__(self, unit_type, name, unit_size, base_points, additional_points):
        pass


class TartarosTerminatorAssaultSquad(TartarosTerminatorSquad):
    def __init__(self, unit_type, name, unit_size, base_points, additional_points):
        pass


class ContemptorDreadnought:
    def __init__(self, unit_type, name, unit_size, base_points, additional_points, weapons_choices):
        self.unit_type = unit_type
        self.name = name
        self.unit_size = unit_size
        self.base_points = base_points
        self.additional_points = additional_points
        self.weapons_choices = weapons_choices
