#!/usr/bin/python3
"""(4) Write a function enzyme_activity(name,subs_conc) that accepts the name of the en-
zyme and substrate concentration as parameters. This will have an inner function called
michelis_menten(Vmax,Km) that computes the reaction rate
v =V max × [S]/Km + [S]
and the outer function should return the reaction rate for given values. Write a main
program that demonstrates the use of this inner and outer function with a meaningful
example."""


def enzyme_activity(name, subs_conc):
    # Inner function for computing rate using Vmax and Km
    def michaelis_menten(Vmax, Km):
        return (Vmax * subs_conc) / (Km + subs_conc)

    # Assume Vmax and Km from literature or arbitrary for demo
    enzyme_data = {"catalase": {"Vmax": 150, "Km": 30},"amylase": {"Vmax": 100, "Km": 50}}
    if name in enzyme_data:
        Vmax = enzyme_data[name]["Vmax"]
        Km = enzyme_data[name]["Km"]
        rate = michaelis_menten(Vmax, Km)
        return f"Reaction rate for {name} at [S]={subs_conc} is {rate:.2f} units"
    else:
        return "Enzyme data not found."


# Example main usage
print(enzyme_activity("catalase", 60))
