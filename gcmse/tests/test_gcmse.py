#!/usr/bin/env python
import gcmse
from scipy import misc

def test_lena_versus_noisy_value_option1():
    lena_ref = misc.imread("gcmse/resources/Lena.png")
    lena_noisy = misc.imread("gcmse/resources/Lena_AdditiveNoise.png")
    my_value = gcmse.GCMSE(lena_ref, lena_noisy, kappa=0.5, option=1)
    assert round(my_value[0]) == 92

def test_lena_versus_noisy_value_option2():
    lena_ref = misc.imread("gcmse/resources/Lena.png")
    lena_noisy = misc.imread("gcmse/resources/Lena_AdditiveNoise.png")
    my_value = gcmse.GCMSE(lena_ref, lena_noisy, kappa=0.5, option=2)
    assert round(my_value[0]) == 80
