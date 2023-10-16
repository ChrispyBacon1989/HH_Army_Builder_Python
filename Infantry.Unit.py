class TroopChoice:
    def __init__(self, unit_type, name, unit_size, base_points, additional_points):
        self.unit_type = unit_type
        self.name = name
        self.unit_size = unit_size
        self.base_points = base_points
        self.additional_points = additional_points


class TacticalSquad(TroopChoice):
    def __init__(self, unit_type, name, unit_size, base_points, additional_points, nuncio_vox, legion_vexilla):
        TroopChoice.__init__(unit_type, name, unit_size, base_points, additional_points)
        unit_type = 'Infantry'
        name = 'Tactical Squad'
        unit_size = 10
        base_points = 100
        additional_points = 0
        self.nuncio_vox = ''
        self.legion_vexilla = ''
    pass

    # self.additional_points = int
    # self.additional_troops = int
    # self.nuncio_vox = bool
    #    if(nuncio_ vox == true):
    #        additional_points + 10

    # self.legion_vexilla = bool
    #    if(legion_vexilla == true):
    #        additional_points +10


NewUnit = TroopChoice('Jump Infantry', 'Assault Squad', 5, 100, 0)

print(NewUnit.unit_type)
print(NewUnit.name)
print(NewUnit.base_points)
print(NewUnit.unit_size)
print(NewUnit.additional_points)

First_Troops = TacticalSquad('Infantry', 'Tactical Squad', 10, 100, 0)

print(First_Troops.unit_type)
