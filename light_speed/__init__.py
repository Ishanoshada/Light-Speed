from math import sqrt, pow, pi
import numpy as np

class LightSpeedPhysics:
    """A comprehensive physics package for light speed and real-world calculations."""

    def __init__(self):
        # Fundamental constants
        self.c = 299792458  # Speed of light in vacuum (m/s)
        self.h = 6.62607015e-34  # Planck constant (J⋅s)
        self.ev_to_joule = 1.602176634e-19  # eV to Joules conversion
        self.epsilon_0 = 8.8541878128e-12  # Vacuum permittivity (F/m)
        self.mu_0 = 1.25663706212e-6  # Vacuum permeability (H/m)

    # Relativistic calculations

    def lorentz_factor(self, velocity):
        beta = velocity / self.c
        if abs(beta) >= 1:
            raise ValueError("Velocity cannot be equal to or greater than the speed of light")
        return 1 / sqrt(1 - pow(beta, 2))

    def time_dilation(self, proper_time, velocity):
        gamma = self.lorentz_factor(velocity)
        return proper_time * gamma

    def length_contraction(self, proper_length, velocity):
        gamma = self.lorentz_factor(velocity)
        return proper_length / gamma

    def relativistic_mass(self, rest_mass, velocity):
        gamma = self.lorentz_factor(velocity)
        return rest_mass * gamma

    def relativistic_momentum(self, mass, velocity):
        gamma = self.lorentz_factor(velocity)
        return mass * velocity * gamma

    def relativistic_kinetic_energy(self, mass, velocity):
        gamma = self.lorentz_factor(velocity)
        return mass * pow(self.c, 2) * (gamma - 1)

    def energy_wavelength_conversion(self, energy_ev):
        energy_joules = energy_ev * self.ev_to_joule
        return (self.h * self.c) / energy_joules

    def doppler_shift(self, frequency, velocity, approaching=True):
        beta = velocity / self.c
        gamma = self.lorentz_factor(velocity)
        if approaching:
            return frequency * gamma * (1 + beta)
        return frequency * gamma * (1 - beta)

    # Optics calculations

    def speed_in_medium(self, refractive_index):
        return self.c / refractive_index

    def refractive_index_calculator(self, material_type):
        indices = {
            'vacuum': 1.0,
            'air': 1.000293,
            'water': 1.333,
            'glass': 1.52,
            'diamond': 2.417,
            'silicon': 3.42
        }
        return indices.get(material_type.lower(), None)

    def snells_law(self, n1, n2, theta1):
        theta1_rad = np.radians(theta1)
        theta2_rad = np.arcsin((n1 * np.sin(theta1_rad)) / n2)
        return np.degrees(theta2_rad)

    def critical_angle(self, n1, n2):
        if n2 >= n1:
            return None  # Total internal reflection impossible
        return np.degrees(np.arcsin(n2 / n1))

    def fiber_optic_travel_time(self, distance, core_index):
        return (distance * core_index) / self.c

    def chromatic_dispersion(self, wavelength1, wavelength2, length, material='silica'):
        B1, B2, B3 = 0.6961663, 0.4079426, 0.8974794
        C1, C2, C3 = 0.0684043, 0.1162414, 9.896161

        def sellmeier(wavelength):
            w2 = wavelength * wavelength
            return sqrt(1 +
                        (B1 * w2) / (w2 - C1) +
                        (B2 * w2) / (w2 - C2) +
                        (B3 * w2) / (w2 - C3))

        n1 = sellmeier(wavelength1)
        n2 = sellmeier(wavelength2)

        return length * abs(n1 - n2) / self.c

    def group_velocity(self, wavelength, dn_dlambda):
        return self.c / (1 - wavelength * dn_dlambda)

    def reflection_coefficient(self, n1, n2, theta_i=0):
        theta_i_rad = np.radians(theta_i)
        theta_t_rad = np.arcsin((n1 * np.sin(theta_i_rad)) / n2)

        r_parallel = ((n2 * np.cos(theta_i_rad) - n1 * np.cos(theta_t_rad)) /
                      (n2 * np.cos(theta_i_rad) + n1 * np.cos(theta_t_rad)))

        r_perpendicular = ((n1 * np.cos(theta_i_rad) - n2 * np.cos(theta_t_rad)) /
                           (n1 * np.cos(theta_i_rad) + n2 * np.cos(theta_t_rad)))

        return r_parallel, r_perpendicular

    def waveguide_modes(self, width, wavelength, n_core, n_cladding):
        V = (2 * pi * width / wavelength) * sqrt(n_core**2 - n_cladding**2)
        return int(V / pi)

