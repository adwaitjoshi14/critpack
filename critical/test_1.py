import critical

def test_crit():
    assert critical.constants('critpack/critical/critical.xlsx',"water") == 'Critical Temperature = 647.096 K and Critical Pressure = 22.064 MPa'
