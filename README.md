## ORBITAL MECHANICS SIMULATOR, SPACE EXPLORATION PROJECT 🚀 🪐 🌱

A Python based space travel simulation calculating orbital velocities for planets in our solar system.

## Features
- Calculates orbital velocities for all 8 planets
- Uses astronomical data and Newtonian physics (circular orbit approximation)
- Foundation for comprehensive space mission planning system

## Current Calculations 
- Mercury through Neptune orbital velocities
- Based on gravitational physics (circular orbits): v = √(GM/r)

## Planned Features
- Moon and ISS orbital data
- Space station logistics planning
- Mission resource management
- Fuel calculations
- Visual orbital simulation

## Technologies
- Python 3
- Mathematics and physics modeling

## How to Run
```bash
python main.py
```

Run a specific section:
```bash
python main.py --section planets
```

Available sections: `all`, `planets`, `earth`, `concepts`, `mars-base`

## Tests
```bash
python3 -m unittest discover -s tests
```

## Data Sources and Assumptions
- Orbital velocities use the circular orbit approximation: `v = sqrt(GM/r)`.
- Gravitational constant `G` uses a rounded CODATA recommended value.
- Planetary semi-major axes are from JPL approximate positions (in AU), converted to meters with the IAU-defined AU.
- Sun mass, Earth mass, Earth mean radius, and Moon mean distance are from NASA fact sheets.
- ISS altitude is a representative average within NASA's reported altitude range.

## Project Structure
- `main.py`: Program entry point
- `constants.py`: Physical constants and reference values
- `data.py`: Orbital datasets and derived distances
- `calculations.py`: Physics calculations and conversions
- `report.py`: Output formatting and section rendering
- `tests/test_calculations.py`: Unit tests for core calculations
