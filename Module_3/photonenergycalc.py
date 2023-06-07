h_Planck = 6.62607015e-34    # J.s
c_light = 299792458          # m/s
e_electron = 1.602176634e-19 # A.s

def photon_energy(wavelength):
    """calculate photon energy in SI"""
    return h_Planck * c_light / wavelength

wavelength_nm = float(input("Enter wavelength in nm -> "))
wavelength = wavelength_nm * 1e-9
energy = photon_energy(wavelength)
energy_eV = energy / e_electron
print(f"Photon with wavelength {wavelength_nm:g} nm has energy {energy_eV:g} eV")
