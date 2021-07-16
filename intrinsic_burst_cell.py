#import numpy as np
#import matplotlib.pyplot as plt

import izhikevich_cells as izh

class ibCell(izh.izhCell):
    def __init__(self,stimVal):
        super().__init__(stimVal)
        # Define Neuron Parameters
        self.celltype='Generic Izhikevich' # Intrinsic Burst 
        self.C=150 
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
        
        def __repr__(self):
            super().__repr__()
            
        def simulate(self): 
            super().simulate() 
        
myCell = ibCell(500) 
myCell.simulate()

if __name__=='__main__': 
    if True: 
        izh.plotMyData(myCell)
        