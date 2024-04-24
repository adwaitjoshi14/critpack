#!/usr/bin/env python
""" finding molar volume """
import pandas as pd
from scipy.optimize import fsolve


def molarvol(path, compound, X):
    "compound is a string which contains the name of compound"
    " X is a list of P and T values fed (float) "
    P, T = X
    df = pd.read_excel(path)
    df.drop(df.columns[0], axis=1, inplace=True)
    comp = compound
    cap = comp.capitalize()
    data = df[df["Name"] == cap]
    Tc = data.iloc[0, 2]
    Pc = data.iloc[0, 3]
    Vc = data.iloc[0, 4]
    w = data.iloc[0, 5]
    k = 0.37464 + 1.54226 * w - 0.26992 * w**2
    Tr = T / Tc
    alpha = (1 + k * (1 - Tr**0.5)) ** 2
    R = 8.314
    b = 0.0778 * R * Tc / (Pc * 1e6)
    a = 0.45724 * R**2 * Tc**2 / (Pc * 1e6)

    def obj(V):
        "function for solving for molar volume"
        z = P * 1e6 - R * T / (V - b) + a * alpha / (V**2 + 2 * b * V - b**2)
        return z

    i = R * T / (P * 1e6)
    sol = fsolve(obj, i)
    Vm = sol[0] * 1e3
    return f"The molar volume is {Vm:1.3f} L/mol"
