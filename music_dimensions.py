import math

class fraction():
    def __init__(self,n,d):
        self.n=n
        self.d=d
        self.reduce()
    def __add__(self,f2):
        n1=self.n
        d1=self.d
        n2=f2.n
        d2=f2.d
        f3=fraction(n1*d2+n2*d1,d1*d2)
        return f3
    def reduce(self):
        pass
    def __str__(self):
        return str(self.n)+"/"+str(self.d)

c = fraction(1,1)
c_s = fraction(139,2187)
d = fraction(1,9)
d_s = fraction(5,32)
e = fraction(27,81)
f = fraction(1,4)
f_s = fraction(217,729)
g = fraction(1,3)
g_s = fraction(2465,6561)
a = fraction(11,27)
a_s = fraction(7,16)
b = fraction(115,243)
total=c + c_s + d + d_s + e + f + f_s + g + g_s + a + a_s + b
print(total)

ionian = c + d + e + f + g + a + b
ion_dis = d + e + a + b
print("Ionian", ionian)

dorian = c + d + d_s + f + g + a + a_s
dor_dis = d + d_s + a + a_s
print("Dorian", dorian)

phyrgian = c + c_s + d_s + f + g + g_s + a_s
phy_dis = c_s + d_s + g_s + a_s
print("Phyrgian", phyrgian)

lydian = c + d + e + f_s + g + a + b
lyd_dis = d + e + a + b
print("Lydian", lydian)

mixolydian = c + d + e + f + g + a + a_s
mix_dis = d + e + a + a_s
print("Mixolydian", mixolydian)

aeolian = c + d + d_s + f + g + g_s + a_s
aeo_dis = d + d_s + g_s + a_s
print("Aeolian", aeolian)

locrian = c + c_s + d_s + f + f_s + g_s + a_s
loc_dis = c_s + d_s + g_s + a_s
print("Ionian", locrian)

ln_serie_error = 1 + 1/2 + 1/3 + 1/4 - math.log(4)

print("Ln error: ", ln_serie_error)

print("Ionian fractal dimension: ", (ion_dis.n/ion_dis.d + ln_serie_error) / math.log(4))

print("Dorian fractal dimension: ", (dor_dis.n/dor_dis.d + ln_serie_error) / math.log(4))

print("Phyrigian fractal dimension: ", (phy_dis.n/phy_dis.d + ln_serie_error) / math.log(4))

print("Mixolydian fractal dimension: ", (mix_dis.n/mix_dis.d + ln_serie_error) / math.log(4))

print("Aeolian fractal dimension: ", (aeo_dis.n/aeo_dis.d + ln_serie_error) / math.log(4))

print("But how to calculate fractal dimensionality of aug 4th and dim 5th for Lydian and Locrian scales?")