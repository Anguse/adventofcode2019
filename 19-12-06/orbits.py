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

def dist_2_san(orbits):
    count = 0
    orbit_relationships = {}
    you_path = []
    san_path = []
    for orbit in orbits:
        planet1,planet2 = orbit.split(')')
        orbit_relationships[planet2] = planet1
    # Get distance from COM to YOU and SAN, individually
    for planet in orbit_relationships.keys():
        if planet == "YOU":
            while planet in orbit_relationships.keys():
                planet = orbit_relationships[planet]
                you_path.append(planet)
        elif planet == "SAN":
            while planet in orbit_relationships.keys():
                planet = orbit_relationships[planet]
                san_path.append(planet)
    # Find where path intersects, the position of this planet is the distance to SAN
    for planet in you_path:
        if planet in san_path:
            count += san_path.index(planet)
            break
        count += 1
    return count
   
if __name__ == '__main__':
    orbits_input = open('input.txt', 'r').read()
    orbits = orbits_input.split('\n')
    count = dist_2_san(orbits)
    print(count)