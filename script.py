import urllib2
import os
url = 'https://ecampus.daiict.ac.in/webapp/intranet/StudentPhotos/'
#import pdb;pdb.set_trace()
for i in range(1,50):
    try:
        filename = '201501'+str(i).zfill(3)+'.jpg'
        file = open(filename,'wb')
        file.write(urllib2.urlopen(url+filename).read())
        file.close()
        print 'File created may be error in URL'
        print filename
    except:
        os.remove(filename)
        print 'Error in URL but removed'
print 'Sucess in downloading'
