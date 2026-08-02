import math
from dataclasses import dataclass


@dataclass(frozen=True)
class SystemConstants:
    MITOCHONDRIAL_MEMBRANE_THICKNESS: float = 5.0e-9
    DIELECTRIC_BREAKDOWN_AIR: float = 3.0e6
    DIELECTRIC_BREAKDOWN_MEMBRANE: float = 5.0e8
    TARGET_DISCHARGE_POWER: float = 1.21e9


@dataclass(frozen=True)
class Vector3D:
    x: float
    y: float
    z: float

    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot_product(self, other: 'Vector3D') -> float:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)


class GAGPEnergeticsEngine:

    def __init__(self, constants: SystemConstants = SystemConstants()):
        self.constants = constants

    def evaluate_membrane_field(self, voltage_millivolts: float) -> dict:
        voltage_volts = voltage_millivolts * 1.0e-3
        thickness = self.constants.MITOCHONDRIAL_MEMBRANE_THICKNESS
        
        field_strength = voltage_volts / thickness if thickness > 0 else 0.0
        ratio_vs_air = field_strength / self.constants.DIELECTRIC_BREAKDOWN_AIR
        ratio_vs_membrane = field_strength / self.constants.DIELECTRIC_BREAKDOWN_MEMBRANE

        return {
            "membrane_voltage_volts": voltage_volts,
            "membrane_thickness_meters": thickness,
            "electric_field_volts_per_meter": field_strength,
            "multiplier_vs_air_breakdown": ratio_vs_air,
            "membrane_dielectric_capacity_used": ratio_vs_membrane
        }

    def evaluate_vector_work_power(self, force_vector: Vector3D, velocity_vector: Vector3D) -> dict:
        force_mag = force_vector.magnitude()
        vel_mag = velocity_vector.magnitude()
        mag_product = force_mag * vel_mag
        
        aligned_power = force_vector.dot_product(velocity_vector)
        
        if mag_product > 0:
            cos_theta_raw = aligned_power / mag_product
            cos_theta_clamped = max(-1.0, min(1.0, cos_theta_raw))
            theta_rad = math.acos(cos_theta_clamped)
        else:
            cos_theta_clamped = 0.0
            theta_rad = 0.0

        theta_deg = math.degrees(theta_rad)

        return {
            "force_magnitude_newtons": force_mag,
            "velocity_magnitude_m_per_s": vel_mag,
            "alignment_angle_radians": theta_rad,
            "alignment_angle_degrees": theta_deg,
            "directional_efficiency_cos_theta": cos_theta_clamped,
            "aligned_power_watts": aligned_power
        }

    def evaluate_high_power_temporal_compression(self, stored_energy_joules: float) -> dict:
        target_power = self.constants.TARGET_DISCHARGE_POWER
        pulse_duration = stored_energy_joules / target_power if target_power > 0 else 0.0

        return {
            "target_power_watts": target_power,
            "stored_energy_joules": stored_energy_joules,
            "required_pulse_duration_seconds": pulse_duration,
            "required_pulse_duration_microseconds": pulse_duration * 1.0e6
        }


def execute_pipeline(
    membrane_mv: float = 200.0,
    force_tuple: tuple = (150.0, 200.0, 50.0),
    velocity_tuple: tuple = (10.0, 12.0, 2.0),
    energy_joules: float = 1210.0
) -> dict:
    """Executes state calculations and returns structural dict with no console IO."""
    engine = GAGPEnergeticsEngine()

    force = Vector3D(*force_tuple)
    velocity = Vector3D(*velocity_tuple)

    return {
        "field_metrics": engine.evaluate_membrane_field(membrane_mv),
        "vector_metrics": engine.evaluate_vector_work_power(force, velocity),
        "discharge_metrics": engine.evaluate_high_power_temporal_compression(energy_joules)
    }
