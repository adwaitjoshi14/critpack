import critical
def test_vol():
    assert critical.molarvol('critpack/critical/critical.xlsx',"nitrogen", [0.101325, 273.15]) == 'The molar volume is 22.395 L/mol'
