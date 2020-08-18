import numpy as np

accepted_particles=['photon', 'electron', 'positron']

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

name_to_mass={'photon': 0,
             'electron': 9.1093837015*10**(-31),
             'positron': 9.1093837015*10**(-31)}

name_to_charge={'photon': 0,
                'electron': -1,
                'positron': 1}

class Particle:
    """Represents a particle with a valid name, total energy in MeV, position 3-vector and a 2-vector direction giving the angles theta and phi in radians"""

    class_counter= 0

    def __init__(self, name, energy, position, direction):

        if name not in accepted_particles:
            raise TypeError("The particle you tried to create is not valid. You can only have: "+str(accepted_particles))
        else:
            self.name = name

        if is_number(energy):
            self.energy = float(energy)
        else:
            raise TypeError("Did not input a number for the energy")

        try:
            iterator = iter(position)
            if len(position)==3:
                self.position = np.array(position).astype('float64')
            else:
                raise TypeError("Did not pass in an iterable of length 3 for the position")
        except TypeError:
            raise TypeError("Did not pass in an iterable of length 3 for the position")

        self.id= Particle.class_counter
        Particle.class_counter += 1

        self.mass = name_to_mass[name]
        self.charge = name_to_charge[name]

        try:
            iterator = iter(direction)
            if len(direction)==2:
                self.direction = np.array(direction).astype('float64')
            else:
                raise TypeError("Did not pass in an iterable of length 2 for the direction")
        except TypeError:
            raise TypeError("Did not pass in an iterable of length 2 for the direction")

    def __repr__(self):
        return str({
            "name":self.name,
            "energy":self.energy,
            "position": self.position,
            "mass": self.mass,
            "direction": self.direction,
            "charge": self.charge,
            "id": self.id
        })
