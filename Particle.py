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

class Particle:
    """Represents a particle with a valid name, energy in Joules, position 3-vector and angle of incidence measured in radians"""
    
    class_counter= 0
    
    def __init__(self, name, energy, position, theta):
        
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
                self.position = position
            else:
                raise TypeError("Did not pass in an iterable of length 3 for the position")
        except TypeError:
            raise TypeError("Did not pass in an iterable of length 3 for the position")
            
        self.id= Particle.class_counter
        Particle.class_counter += 1
        
        self.mass = name_to_mass[name]
        
        if is_number(theta):
            self.theta = float(theta)
        else:
            raise TypeError("Did not input a number for the angle of incidence")
