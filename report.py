from calculations import calculate_orbital_velocity, meters_to_km
from data import CONCEPT_STATIONS, EARTH_ORBITS, ISS_TO_MOON_DISTANCE, PLANETS

LABEL_WIDTH = 30
VALUE_WIDTH = 10


def print_section(title):
    print(title)


def print_metric(label, value, unit="", note=""):
    label_text = f"{label}:".ljust(LABEL_WIDTH)
    value_text = f"{value:>{VALUE_WIDTH}}"
    unit_text = f" {unit}" if unit else ""
    note_text = f" ({note})" if note else ""
    print(f"{label_text}{value_text}{unit_text}{note_text}")


def render_planet_velocities():
    print_section("--PLANET ORBITAL VELOCITY DATA--")
    for name, orbital_radius, central_mass in PLANETS:
        velocity_km = calculate_orbital_velocity(orbital_radius, central_mass)
        print_metric(f"{name} orbital velocity", f"{velocity_km:.2f}", "km/s")


def render_earth_orbits():
    print_section("--EARTH ORBITAL SYSTEMS--")
    for name, orbital_radius, central_mass, kind in EARTH_ORBITS:
        velocity_km = calculate_orbital_velocity(orbital_radius, central_mass)
        print_metric(f"{name} orbital velocity", f"{velocity_km:.2f}", "km/s", kind)

    iss_to_moon_km = meters_to_km(ISS_TO_MOON_DISTANCE)
    print_metric("ISS distance from Moon", f"{iss_to_moon_km:.0f}", "km")


def render_concept_stations():
    print_section("--CONCEPT STATIONS--")
    for name, midpoint_distance, note in CONCEPT_STATIONS:
        midpoint_km = meters_to_km(midpoint_distance)
        print_metric(f"Concept station {name}", f"{midpoint_km:.0f}", "km", note)


def render_mars_base_concept():
    print_section("--MARS BASE CONCEPT--")
    print("Location: Unknown")
    print("Core Infrastructure:")
    print(" - Central Human Center (?m living space)")
    print(" - Structure: Habitat modules, life support, power, landing pad, Bunkers")
    print("Life Support Systems:")
    print(" - Systems: Radiation shield, water extraction, O2 generation")
    print(" - Food production (supplemental Earth shipments)")
    print("Power Generation:")
    print(" - Primary: Nuclear reactors")
    print(" - Secondary: Solar arrays")
    print(" - Emergency: Battery storage")
    print("Protection Systems:")
    print(" - Pressure leak detection and auto-seal")
    print(" - Dust mitigation airlocks")
    print(" - Emergency evacuation protocols")
    print("Crew Capacity: ?")
    print("Mission Duration: ?")
