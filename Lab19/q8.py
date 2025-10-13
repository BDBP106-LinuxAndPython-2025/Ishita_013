#!/usr/bin/python3
"""Write a function protein_energy(temp) with an inner function
calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0)."""

def protein_energy(temp):
    def calculate_free_energy(enthalpy, entropy):
        g = enthalpy - (temp * entropy)
        return9 g, "stable" if g < 0 else "unstable"
    return calculate_free_energy

protein_energy(300)
