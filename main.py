import argparse

from report import (
    render_concept_stations,
    render_earth_orbits,
    render_mars_base_concept,
    render_planet_velocities,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Orbital mechanics simulator and space exploration report."
    )
    parser.add_argument(
        "--section",
        choices=["all", "planets", "earth", "concepts", "mars-base"],
        default="all",
        help="Select which section to display.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print("--PLANET ORBITAL SIMULATION & SPACE EXPLORATION GUIDE--")
    print("Project Summary: planet data, sustainability & space travel concepts - 🚀 🪐 🌱 ")

    sections = {
        "planets": render_planet_velocities,
        "earth": render_earth_orbits,
        "concepts": render_concept_stations,
        "mars-base": render_mars_base_concept,
    }

    if args.section == "all":
        for renderer in sections.values():
            renderer()
    else:
        sections[args.section]()


if __name__ == "__main__":
    main()
