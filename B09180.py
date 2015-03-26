#!/usr/bin/env python
import os
import sys
    
def search():
    """
    entrée: tableau de m/z représentant une acquisition (spectre MS)
    sortie: tableau avec pour chaque m/z de la librairie de composé,
    son nom et les m/z d'acquisition correspondant, à une tolérance près.
    """
    #librairie de composés: format: name:m/z (masse monoisotopique en Dalton)"
    compound_base = {'carbone':7.016004, 'oxygène':15.99491463, 'butane':58.078251, 'hexane':86.109550}
    print('Librairie\nm/z\tnom')
    for k, v in compound_base.items():
        print(k, v)
    # acquisition: format: m/z (monoisotopic mass in Da)"
    acq = [7, 15.5, 60] 
    print('\nAcquisition (tableau de m/z (en Da))')
    print(acq)
    #tolérance en Dalton
    tol = 30

    print('\nm/z acq\tnom\tm/z')
    for mz in acq:
        for k, v in compound_base.items():
            if (v - tol) <= mz and mz <= (v + tol):
                print(str(mz)+'\t'+str(k)+'\t'+str(v))
if __name__ == "__main__":
    search()

    
    
