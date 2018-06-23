from astropy.io import fits
from PIL import Image
import numpy as np


ims=Image.open("/users/wangfeng/desktop/天算法/me.jpg").convert("L")
hdu = fits.PrimaryHDU(ims)
hdu3=fits.TableHDU()
print(type(hdu),'\n',hdu)
# hdulist = fits.HDUList([hdu])
# hdulist.writeto('new1.fits')
# hdu.writeto('ne6.fits')
hdu1=fits.open('new1.fits',mode='update')
hdu1.info()
head=hdu1[0].header
head.set('TITLE','Myself','Handsome as I am')
head.set('MODEL','Che1-CL10','Honor 4X')
head.set('DATE','2017-4-29','Photo: Creation Date')
head.set('EXPOSURE','1/120','Unit: s')
head.set('APERTURE','2.4','Aperture Value')
head.set('IOS','100','None')
head.set('FL','22','FL: Focal length  Unit: mm')
head.set('WB','Auto','WB: White balance')
head.set('FLASH','No flash','None')

data1=np.array(['Exif Version','FlashPix Version'])
data2=np.array(['1.00','2.4'])
col1 = fits.Column(name='property', format='20A', array=data1)
col2 = fits.Column(name='parament', format='20A', array=data2)
cols = fits.ColDefs([col1, col2])
tbhdu = fits.TableHDU.from_columns(cols)
tbhdu.update('new1.fits')
hdu1.info()
print(hdu1[0].header)
hdu1.flush()
# hdu1.writeto('new2.fits')
# hdu1.close()