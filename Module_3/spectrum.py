# calculate the energy across the visible spectrum for different colors
# see https://en.wikipedia.org/wiki/Visible_spectrum#Spectral_colors

import photonenergycalc

def J2eV(energy):
    """Convert energy from J to eV"""
    return energy / photonenergycalc.e_electron

# from https://en.wikipedia.org/wiki/Visible_spectrum
colors = [("red", (625, 750)),
          ("orange", (590, 625)),
          ("yellow", (565, 590)),
          ("green", (500, 565)),
          ("cyan", (485, 500)),
          ("blue", (450, 485)),
          ("violet", (380, 450))]

if __name__ == "__main__":

    # compute energies corresponding toe lower and upper wavelengths
    # 1. convert input wavelength nm to m
    # 2. convert output energy from J to eV
    energies = [(J2eV(photonenergycalc.photon_energy(lambdas[0] * 1e-9)),
                 J2eV(photonenergycalc.photon_energy(lambdas[1] * 1e-9)))
                for name, lambdas in colors]

    # iterate through colors and energies together (in reverse order
    # so that violet is at top) to pull out the relevant data and
    # pretty print (note that lower energy belongs to higher wavelength!)

    header = "{name:10s} {wavelength:12s} {energy:9s}".format(
        name="color", wavelength="wavelength (nm)", energy="energy (eV)")
    print(header)
    print("-" * len(header))
    for (name, lambdas), energies in zip(reversed(colors),
                                       reversed(energies)):
        print(f"{name:10s}     "
              f"{lambdas[0]:3g}-{lambdas[1]:3g}      "
              f"{energies[1]:4.2f}-{energies[0]:4.2f}")

