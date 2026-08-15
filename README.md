# 🚀 Mega Engineering Library (englib)

The ultimate, ultra-high-performance open-source computing library that unifies core formulas, analytical models, and computational tools from **22 distinct engineering disciplines** under a single, highly optimized hybrid architecture powered by **Python** and **Rust**.

---

## 🏛️ Core Architecture & Philosophical Vision

Historically, the engineering world has been highly fragmented across isolated computational software ecosystems. Mechanical engineers rely heavily on MATLAB, civil structural engineers deploy independent finite element packages, while software developers build bespoke micro-services from scratch. This fragmentation leads to massive data format incompatibilities, bloated dependency graphs, and multi-million dollar annual software licensing overheads for small-to-medium enterprises (SMEs) and research labs.

**`mega_engineering_library` (englib)** smashes these interdisciplinary silos. It establishes a unified, cross-functional open-source library where high-tech modern projects—such as autonomous electric drones, biomedical prosthetics, or chemical production lines—can instantly import exact mathematical validations from a single repository.

### 📐 System Architecture Diagram

Below is the conceptual framework showing how end-users interact with the high-level Python package while heavy multi-dimensional calculations are routed down to the silicon layer via native Rust extensions:

```text
       ┌────────────────────────────────────────────────────────┐
       │                   END-USER APPLICATION                 │
       └───────────────────────────┬────────────────────────────┘
                                   │
                     import englib.[discipline]
                                   │
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │             PYTHON HIGH-LEVEL WRAPPER INTERFACE        │
       │  (Aerospace, Civil, Mechanical, Geomatics, etc.)       │
       └───────────────────────────┬────────────────────────────┘
                                   │
                    Strict Boundary & Safety Guards
                    (Exceptions: PhysicalBoundaryError)
                                   │
                                   ▼
          ================== PyO3 BINDINGS LAYER ==================
                                   │
                        Direct C-ABI Memory Maps
                                   │
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │                NATIVE RUST CORE COMPUTATION ENGINE     │
       │    [matrix.rs]    [calculus.rs]    [solvers.rs]        │
       │               [fem_solver.rs]  [cfd_solver.rs]         │
       └────────────────────────────────────────────────────────┘
                                   │
                     Hardware Level Multi-Threading
                                   ▼
          ================== HARDWARE (CPU/SILICON) ==================
```

### ⚡ Technical Pillars
*   **Hardware-Accelerated Math Core:** Heavy numerical tasks like multi-dimensional matrix multiplications, discrete derivatives, trapezoidal integrations, and non-linear root-finding algorithms are shifted down to the silicon layer via the native **Rust Core Engine (`core/`)** using PyO3 bindings.
*   **Lazy-Loaded Zero-Bloat Modularity:** Implements loose coupling architectures. If an engineer executes a script utilizing `englib.civil`, Python only initializes the civil engineering namespace inside the RAM. The other 21 massive disciplines remain fully dormant, ensuring a lightweight, minimal memory footprint.
*   **Academic-Grade Failure Guards:** Every single function is bounded by custom failure exceptions (e.g., `PhysicalBoundaryError`, `GeometricViolationError`). Calculations will automatically abort with strict error logs before code execution if physical metrics violate the laws of nature (e.g., negative mass, absolute zero violations, or over-reinforced concrete stress boundaries).

---

## 🗺️ Completed Ecosystem Map (The 22 Disciplines)

Every single module listed below is structurally complete, fully documented, and mapped to the central library wrapper interface:

*   📂 **`aerospace` (Aerospace Engineering)**: Fluid-wing lift/drag mechanics, elliptical Vis-Viva orbital velocities, Tsiolkovsky rocket Delta-V equations, and X-band radar range tracking.
*   📂 **`agricultural` (Agricultural Engineering)**: Quartz bulk soil porosities, volumetric water retention profiles, Rational method peak surface runoffs, and machinery drawbar power pulling forces.
*   📂 **`biomedical` (Biomedical Engineering)**: Orthopedic bone axial stress limits, human physiological ECG/EEG heart rate RR-intervals, and in-vivo biomaterial degradation depths.
*   📂 **`chemical` (Chemical Engineering)**: Arrhenius reaction kinetics thermal rates, Continuous Stirred-Tank Reactor (CSTR) sizing, Fickian molecular diffusion fluxes, and process heat exchanger LMTD tracking.
*   📂 **`civil` (Civil Engineering)**: Simply supported beam reaction forces, structural natural periods, Equivalent Lateral seismic Base Shear, ACI concrete steel reinforcement ratios, Euler column buckling, Terzaghi shallow footing geotechnical capacities, and Manning open channel hydraulics.
*   📂 **`computer` (Computer Engineering)**: Parallel multi-core Amdahl's scaling laws, packet teletraffic Little queuing buffers, modular RSA cryptographic exponentiations, and PCB high-speed microstrip characteristic impedances.
*   📂 **`electrical` (Electrical Engineering)**: Multi-parameter active Ohm's law, series/parallel resistor grids, Nyquist signal anti-aliasing sampling rates, three-phase apparent power, and classical parallel closed-loop PID control outputs.
*   📂 **`environmental` (Environmental Engineering)**: Atmospheric Gaussian plume dispersion concentrations, Streeter-Phelps river dissolved oxygen deficits, LandGEM landfill bio-gas decay kinetics, and porous aquifer contaminant seepage velocities.
*   📂 **`food` (Food Engineering)**: Microbial thermal destruction D-values, and non-Newtonian Ostwald-de Waele Power Law food fluid rheology shear stresses.
*   📂 **`geomatics` (Geomatics Engineering)**: WGS84 planetary reference ellipsoid flattening indexes, Geodetic-to-ECEF Cartesian conversions, and drone photogrammetric camera image scale metrics.
*   📂 **`industrial` (Industrial Engineering)**: Resource allocation linear programming objective models, stochastic M/M/1 queuing arrivals, supply chain economic order quantities (EOQ), and Six Sigma process capability (Cp) manufacturing tolerances.
*   📂 **`marine` (Marine Engineering)**: Metacentric height initial ship floating stabilities, wave-making resistance Froude scaling, propeller advance coefficients, and wave-induced structural midship bending moments.
*   📂 **`materials` (Materials Science)**: Bragg atomic interplanar spacings via X-ray diffraction, Griffith critical fracture stresses for brittle cracks, binary alloy phase diagram Lever Rule weight fractions, and macromolecular polydispersity indexes (PDI).
*   📂 **`mechanical` (Mechanical Engineering)**: Fluid mechanics flow regimes, Rankine power cycles, Mohr's circle stress transformations, Fourier plane wall thermal conductions, solid shaft elastic torsions, and rolling-element bearing life hours.
*   📂 **`metallurgical` (Metallurgical Engineering)**: Extractive pyrometallurgy slag basicity ratios, and Avrami solid-state alloy phase transformation kinetics.
*   📂 **`mining` (Mining Engineering)**: Hoek-Brown rock mass uniaxial tensile strengths, explosive charge detonation pressures, Atkinson airway ventilation friction losses, and spatial ore resource estimations using Inverse Distance Weighting (IDW).
*   📂 **`nuclear` (Nuclear Engineering)**: Fission chain reaction Six-Factor multiplication factors, fuel rod cladding surface heat fluxes, exponential gamma radiation attenuation shielding barriers, and Tokamak plasma Lawson criterion products.
*   📂 **`petroleum` (Petroleum Engineering)**: Fluid PVT gas-oil production ratios, Archie petrophysical water saturation log interpretations, Vogel inflow performance relationships (IPR), and drilling mud dynamic equivalent circulating densities (ECD).
*   📂 **`software` (Software Engineering)**: COCOMO II post-architecture software project effort person-months calculations, and McCabe structural control flow graph cyclomatic software risks indexing.
*   📂 **`systems` (Systems Engineering)**: System reliability mean time between failures (MTBF) tracking and macro structural systems architecture verification frameworks.
*   📂 **`textile` (Textile Engineering)**: Fiber fractional moisture regains, yarn structural twist multiplier tex linear densities, and structural fabric Peirce cloth yarn crimp fractions.
*   📂 **`transportation` (Transportation Engineering)**: Greenshields traffic stream flow speeds, AASHTO multi-layer flexible pavement structural numbers, and geometric highway alignment stopping sight distances (SSD).

---

## 🛠️ Quick Start & Developer Installation

Since `englib` utilizes a high-performance native Rust core backend, compiling the extension module requires Rust tools configured on your deployment system.

```bash
# Clone the unified multi-disciplinary repository
git clone https://github.com/yagizyagli/mega_engineering_library
cd mega_engineering_library

# Install the library locally in editable developer mode (compiles the Rust core engine automatically)
pip install -e .
```

### Production Code Example

```python
from englib.mechanical.fluid_mechanics import FluidMechanics
from englib.civil.statics import CivilStatics

# 1. Calculate fluid pipeline flow dynamics regimes
reynolds = FluidMechanics.calculate_reynolds_number(
    velocity=2.5, 
    diameter=0.08, 
    kinematic_viscosity=1e-6
)
print(f"Calculated Pipe Reynolds Number: {reynolds}")

# 2. Compute exact structural support loads for automated civil designs
left_rx, right_rx = CivilStatics.solve_simply_supported_beam_reactions(
    length=12.0, 
    point_load=150.0, 
    load_position=6.0
)
print(f"Symmetrical Beam Support Reactions: {left_rx} kN, {right_rx} kN")
```

---

## 🧪 Rigorous Academic Testing

Every discipline is accompanied by a dedicated validation module verifying numerical consistency against real university exam and textbook benchmarks.

```bash
# Run the entire academic validation testing suite via pytest
pytest tests/
```

---

## 🤝 Contribution Guidelines

We welcome global experts, professional engineers, and academic researchers to expand this ecosystem. Please refer to our automated `PULL_REQUEST_TEMPLATE.md` when proposing new equations. Every contribution **must** cite a valid academic standard or reference textbook (with page and equation tracking) to pass maintainer reviews.

---

## 📜 License & Copyright

Distributed under the **Apache License 2.0**. See `LICENSE` for more information.

This license allows absolute commercial usage, corporate proprietary integration, and open academic redistribution while offering strict defensive patent protection safeguards for the initial contributors.

## 👑 Author & Founder
*   **Yağız Yağlı** ([@yagizyagli](https://github.com/yagizyagli))
*   *Feel free to reach out for global academic collaborations, institutional deployments, or multi-disciplinary research initiatives.*

---

## ⭐ Support the Project!
If you find this massive multi-disciplinary library useful for your academic research, industrial projects, or hardware simulations, **please give this repository a STAR!** It helps increase global visibility and attracts more expert contributors to our ecosystem.
