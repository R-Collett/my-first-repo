import numpy
import kwant

print("Hello from Binder!")

syst = make_system()
smatrix = kwant.smatrix(syst)
G = smatrix.transmission(1,0)
