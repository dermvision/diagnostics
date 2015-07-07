import urllib, urllib2, os

domain = 'http://www.dermoscopyatlas.com/'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
req = urllib2.Request(os.path.join(domain, 'diagindex.cfm'), headers=hdr)
page = urllib2.urlopen(req).readlines()
for line in page:
	if 'diagdetail.cfm?id=' in line:
		disease = line.split('">')[1].split('</a>')[0].strip('.')
		dis_id = int(line.split('"')[1].split('=')[-1])
		print disease
		dis_link = 'http://www.dermoscopyatlas.com/diagdetail.cfm?id={}'.format(dis_id)
		req2 = urllib2.Request(dis_link, headers=hdr)
		page2 = urllib2.urlopen(req2).readlines()
		for line2 in page2:
			if 'http://www.dermoscopyatlas.com/upload/' in line2:
				img_found = True
				i = line2.split('http://www.dermoscopyatlas.com/upload/th')[1].split('_')[0]
				if not os.path.exists(disease): os.makedirs(disease)
				j = 0
				while img_found is True:
					j += 1
					img = '{}_{}.jpg'.format(i, j)
					img_link = 'http://www.dermoscopyatlas.com/upload/' + img
					(tmp, info) = urllib.urlretrieve(img_link, os.path.join(disease, img))
					print info
					if 'image' not in info['Content-Type']: 
						img_found = False
						os.remove(os.path.join(disease, img))
