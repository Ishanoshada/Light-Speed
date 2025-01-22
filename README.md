# Light Speed Physics

`light_speed` is a comprehensive Python package for calculations and simulations related to the speed of light, relativistic physics, and real-world optical phenomena. It is designed for scientists, researchers, and physics enthusiasts who want to explore the fascinating world of light and its interactions.

---

## Features

- **Relativity Calculations**:
  - Lorentz factor, time dilation, length contraction, relativistic mass, and momentum.
- **Optics**:
  - Snell's law, critical angle, and chromatic dispersion in fiber optics.
- **Photon Energy**:
  - Energy-wavelength conversions.
- **Waveguides**:
  - Supported modes in planar waveguides.
- **Medium Properties**:
  - Speed of light in various mediums, refractive index calculators, and Fresnel reflection coefficients.

---

## Installation

Install the package using pip:

```bash
pip install light_speed
```

---

## Usage

### Import the Package
```python
from light_speed import LightSpeedPhysics
```

### Examples

### **1. Speed of Light in a Medium**
Calculate the speed of light in a specific medium using its refractive index:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
n_water = physics.refractive_index_calculator('water')
speed_water = physics.speed_in_medium(n_water)
print(f"Speed of light in water: {speed_water:.2f} m/s")
```

---

### **2. Relativistic Time Dilation**
Compute the time dilation for an object moving at a significant fraction of the speed of light:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
proper_time = 1.0  # seconds
velocity = 1e7  # m/s
dilated_time = physics.time_dilation(proper_time, velocity)
print(f"Dilated Time: {dilated_time:.2f} seconds")
```

---

### **3. Lorentz Factor**
Calculate the Lorentz factor for a given velocity:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
velocity = 1e7  # m/s
lorentz_factor = physics.lorentz_factor(velocity)
print(f"Lorentz Factor: {lorentz_factor:.2f}")
```

---

### **4. Length Contraction**
Find the contracted length of a moving object:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
proper_length = 10.0  # meters
velocity = 2e8  # m/s
contracted_length = physics.length_contraction(proper_length, velocity)
print(f"Contracted Length: {contracted_length:.2f} meters")
```

---

### **5. Relativistic Mass**
Calculate the relativistic mass of an object:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
rest_mass = 70.0  # kg
velocity = 2.5e8  # m/s
rel_mass = physics.relativistic_mass(rest_mass, velocity)
print(f"Relativistic Mass: {rel_mass:.2f} kg")
```

---

### **6. Relativistic Momentum**
Determine the relativistic momentum of a moving object:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
mass = 70.0  # kg
velocity = 2.5e8  # m/s
momentum = physics.relativistic_momentum(mass, velocity)
print(f"Relativistic Momentum: {momentum:.2e} kg⋅m/s")
```

---

### **7. Relativistic Kinetic Energy**
Calculate the kinetic energy of an object moving at relativistic speeds:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
mass = 70.0  # kg
velocity = 2e8  # m/s
kinetic_energy = physics.relativistic_kinetic_energy(mass, velocity)
print(f"Relativistic Kinetic Energy: {kinetic_energy:.2e} Joules")
```

---

### **8. Energy to Wavelength Conversion**
Convert photon energy (in electron volts) to wavelength:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
energy_ev = 2.0  # eV
wavelength = physics.energy_wavelength_conversion(energy_ev)
print(f"Wavelength: {wavelength:.2e} meters")
```

---

### **9. Snell's Law**
Calculate the angle of refraction when light moves between two mediums:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
theta1 = 30  # degrees
n1 = physics.refractive_index_calculator('air')
n2 = physics.refractive_index_calculator('glass')
theta2 = physics.snells_law(n1, n2, theta1)
print(f"Refraction Angle: {theta2:.2f} degrees")
```

---

### **10. Critical Angle**
Determine the critical angle for total internal reflection:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
critical_angle = physics.critical_angle(1.52, 1.000293)
print(f"Critical Angle: {critical_angle:.2f} degrees")
```

---

### **11. Fiber Optic Travel Time**
Calculate the travel time of light through a fiber optic cable:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
distance = 100000  # meters
core_index = 1.462
travel_time = physics.fiber_optic_travel_time(distance, core_index)
print(f"Travel Time: {travel_time * 1000:.2f} milliseconds")
```

---

### **12. Chromatic Dispersion**
Calculate the time delay caused by chromatic dispersion in optical fibers:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
wavelength1 = 1.55e-6  # meters
wavelength2 = 1.50e-6  # meters
fiber_length = 50000  # meters
time_delay = physics.chromatic_dispersion(wavelength1, wavelength2, fiber_length)
print(f"Chromatic Dispersion Time Delay: {time_delay:.2e} seconds")
```

---

### **13. Group Velocity**
Compute the group velocity of a light pulse in a medium:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
wavelength = 1.55e-6  # meters
dn_dlambda = -0.02  # change in refractive index per wavelength
group_velocity = physics.group_velocity(wavelength, dn_dlambda)
print(f"Group Velocity: {group_velocity:.2f} m/s")
```

---

### **14. Fresnel Reflection Coefficient**
Calculate the Fresnel reflection coefficients:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
n1 = 1.000293  # air
n2 = 1.52  # glass
theta_i = 45  # degrees
r_parallel, r_perpendicular = physics.reflection_coefficient(n1, n2, theta_i)
print(f"Reflection Coefficient (Parallel): {r_parallel:.2f}")
print(f"Reflection Coefficient (Perpendicular): {r_perpendicular:.2f}")
```

---

### **15. Waveguide Modes**
Calculate the number of modes supported by a planar waveguide:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
width = 5e-6  # meters
wavelength = 1.55e-6  # meters
n_core = 1.5
n_cladding = 1.4
modes = physics.waveguide_modes(width, wavelength, n_core, n_cladding)
print(f"Number of Modes: {modes}")
```

---

### **16. Doppler Shift**
Calculate the relativistic Doppler shift for an approaching or receding source:
```python
from light_speed import LightSpeedPhysics

physics = LightSpeedPhysics()
frequency = 500e12  # Hz
velocity = 2e7  # m/s
approaching = True  # True if approaching, False if receding
shifted_frequency = physics.doppler_shift(frequency, velocity, approaching)
print(f"Shifted Frequency: {shifted_frequency:.2f} Hz")
```


---
## Requirements

- Python 
- NumPy (automatically installed)

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



**Repository Views** ![Views](https://profile-counter.glitch.me/lights/count.svg)
