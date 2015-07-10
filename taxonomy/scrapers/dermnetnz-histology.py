import urllib, urllib2, os
rootdir = 'dermnetnz-histology'
if not os.path.exists(rootdir): os.makedirs(rootdir)

domain = 'http://www.dermnetnz.org/'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(os.path.join(domain, 'pathology'), headers=hdr)
page = urllib2.urlopen(req).readlines()
for line in page:
	if '<a href="' in line:
		link = line.split('"')[1]
		if '/pathology/' in link:
			dislink = os.path.basename(link)
			disease = dislink.split('.')[0].split('-path')[0]
			disdir = os.path.join(rootdir, disease)
			if not os.path.exists(disdir): os.makedirs(disdir)
			# print disease
			link = os.path.join(domain, 'pathology', dislink)
			req2 = urllib2.Request(link, headers=hdr)
			
			try:
				page2 = urllib2.urlopen(req2).readlines()
			except:
				continue
			
			for line2 in page2:
				if '<img src="/pathology/img/' in line2:
					img = line2.split('src=')[1].split('"')[1]
					img = img.replace('-sm', '')
					imgfile = os.path.basename(img)
					imgpath = os.path.join(disdir, imgfile)
					imglink = os.path.join(domain, img[1:])
					
					print 'wget -O {} {}'.format(imgpath, imglink)
