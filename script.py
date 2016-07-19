import urllib2
import os
try:
    url = '201501300.jpg'
    file = open(url,'wb')
    file.write(urllib2.urlopen('https://ecampus.daiict.ac.in/webapp/intranet/StudentPhotos/'+url).read())
    file.close()
    print 'File created may be error in URL'
except:
    os.remove(url)
    print 'Error in URL but removed'
