import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np

hdu=fits.open("spSpec-51612-0280-152.fit")
hdu.info()
print(hdu[0].header)

lglambda0=np.array(hdu[0].header['coeff0'])
lgdeltalambda=np.array(hdu[0].header['coeff1'])
N=np.array(hdu[0].header['naxis1'])
lambdan=np.array([i for i in range(N)])

wave=10**(lglambda0+lambdan*lgdeltalambda)
flux=hdu[0].data[0]
CSS=hdu[0].data[1]
err=hdu[0].data[2]


plt.plot(wave,flux,color='gray',linewidth=0.2)
plt.plot(wave,err,color='k',linewidth=0.2)
plt.plot(wave,CSS,color='b',linewidth=0.2)
plt.legend()
plt.show()

