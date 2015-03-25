from django.db import models

# Create your models here.

class Compound(models.Model):
    # chemical formular
    formula = models.CharField(max_length=32)
    # monoisotopic molecular weight (in Dalton)
    # no rounding error with decimal (compared with float)
    mw = models.DecimalField(max_digits=10, decimal_places=6)
    name = models.CharField(max_length=128)
    # CAS number of the compound (10 digits + 2 hyphens)
    cas = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.name

    
