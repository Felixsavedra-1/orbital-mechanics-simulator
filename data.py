from constants import AU, EARTH_MASS, EARTH_RADIUS, ISS_ALTITUDE, MOON_ORBITAL_RADIUS, SUN_MASS


# Semi-major axis values (AU), source: JPL approximate positions of major planets
PLANET_SEMIMAJOR_AXIS_AU = [
    ("Mercury", 0.38709927),
    ("Venus", 0.72333566),
    ("Earth", 1.00000261),
    ("Mars", 1.52371034),
    ("Jupiter", 5.20288700),
    ("Saturn", 9.53667594),
    ("Uranus", 19.18916464),
    ("Neptune", 30.06992276),
]

PLANETS = [(name, axis_au * AU, SUN_MASS) for name, axis_au in PLANET_SEMIMAJOR_AXIS_AU]

EARTH_ORBITS = [
    ("Moon", MOON_ORBITAL_RADIUS, EARTH_MASS, "Natural satellite"),
    ("ISS", EARTH_RADIUS + ISS_ALTITUDE, EARTH_MASS, "Space station"),
]

ISS_TO_MOON_DISTANCE = MOON_ORBITAL_RADIUS - (EARTH_RADIUS + ISS_ALTITUDE)

EARTH_ORBITAL_RADIUS = PLANETS[2][1]
MARS_ORBITAL_RADIUS = PLANETS[3][1]
MARS_EARTH_MIN_DISTANCE = MARS_ORBITAL_RADIUS - EARTH_ORBITAL_RADIUS

CONCEPT_STATIONS = [
    ("Earth-Moon midpoint", MOON_ORBITAL_RADIUS / 2, "Based on average Earth-Moon distance"),
    ("Earth-Mars midpoint", MARS_EARTH_MIN_DISTANCE / 2, "Based on minimum Earth-Mars distance"),
]
