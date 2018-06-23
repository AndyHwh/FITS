from astropy.io import fits
from PIL import Image
import numpy as np

###载入图片
ims=Image.open("/users/wangfeng/desktop/天算法/me1.jpeg").convert("L")

###创建头文件数据（Data）
hdu = fits.PrimaryHDU(ims)
print(type(hdu))
hdu3=fits.TableHDU()

###创建扩展单元数据（Data）
data1=np.array(['Color Space','Exif Version','FlashPix Version','Date Time Digitized',
                'Date Time Original','Gain Control','Megapixels','Compression'])
data2=np.array(['sRGB','2.20','1.00','Sun Dec 8 2002 12:00:00 pm','Sat Apr 29 2017 3:45:52 pm',
                'Low gain up','2.12 mp','JPEG(old-style)'])
col1 = fits.Column(name='property', format='20A', array=data1)
col2 = fits.Column(name='parament', format='20A', array=data2)
cols = fits.ColDefs([col1, col2])
tbhdu = fits.TableHDU.from_columns(cols)
hdulist = fits.HDUList([hdu])

hdulist.append(tbhdu)
# hdulist.writeto('personal.fits')
hdu1=fits.open('personal.fits',mode='update')

###写入主单元头文件
head=hdu1[0].header
print(type(hdu1[0].data))
head.set('TITLE','Myself','Handsome as I am')
head.set('MAKE','HUAWEI','None')
head.set('MODEL','Che1-CL10','Honor 4X')
head.set('DATE','2017-4-29','Photo: Creation Date')
head.set('EXPOSURE','1/120','Unit: s')
head.set('APERTURE','2.4','Aperture Value')
head.set('IOS','100','None')
head.set('FL','22','FL: Focal length  Unit: mm')
head.set('WB','Auto','WB: White balance')
head.set('FLASH','No flash','None')
head.set('EI','218','EI: Exposure Index')

###写入扩展单元头文件（命名该扩展单元）
head=hdu1[1].header.set('EXTNAME','Image.Info','FITS: Name of Table')

hdu1.info()
print(hdu1[0].header,'\n',hdu1[1].header,'\n',hdu1[1].data[0])
hdu1.flush()
# hdu1.writeto('new2.fits')
hdu1.close()