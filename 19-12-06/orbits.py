import string

def count_orbits(orbits):
    count = 0
    orbit_relationships = {}
    for orbit in orbits:
        planet1,planet2 = orbit.split(')')
        orbit_relationships[planet2] = planet1
    for planet in orbit_relationships.keys():
        while planet in orbit_relationships.keys():
            planet = orbit_relationships[planet]
            count += 1
    return count
   
if __name__ == '__main__':
    orbits_input = open('input.txt', 'r').read()
    orbits = orbits_input.split('\n')
    count = count_orbits(orbits)
    print(count)