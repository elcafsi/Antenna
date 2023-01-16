import numpy 
import matplotlib.pyplot as plt 
# pi math
pi=numpy.pi
# distance between antennas
d=0.5
# Number of antennas
N=8
# Elevation angle theta 
theta=numpy.arange(-180,180,1)*pi/180

factor=0

for i in range (1,N):
    factor = factor + numpy.exp(1j*2*pi*d*i*numpy.sin(theta))

factor=1+factor
factor=abs(factor)/max(factor)
factor=10*numpy.log10(factor)


plt.title("Normalized Radiation Pattern of antenna array")
plt.ylim(-30,0)
plt.xlim(-90,90)
plt.plot(theta*180/pi,factor)

plt.show()

