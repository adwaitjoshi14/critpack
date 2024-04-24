#!/usr/bin/env python
""" finding the critical constants """

import pandas as pd
def constants(path, compound):
    'path is the path to the excel file'
    'compound is a string which contains the name of compound'
    df = pd.read_excel(path)
    df.drop(df.columns[0], axis=1, inplace=True)
    comp = compound
    cap = comp.capitalize()
    data = df[df["Name"] == cap]
    Tc = data.iloc[0, 2]
    Pc = data.iloc[0, 3]
    Vc = data.iloc[0, 4]
    w = data.iloc[0, 5]
    return (f'Critical Temperature = {Tc} K and Critical Pressure = {Pc} MPa')

