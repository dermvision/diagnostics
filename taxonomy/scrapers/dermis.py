import urllib2, os, string, urllib
domain = 'http://www.dermis.net'
site = urllib2.urlopen(domain+'/dermisroot/en/list/all/search.htm').readlines()
for line in site:
	for line2 in line.split('<li>'):
		if '<a href=' in line2 and 'diagnose.htm' in line2:
			img_dir = string.join(line2.split('>')[1].split()[:-2])
			print img_dir
			if not os.path.exists(img_dir): os.makedirs(img_dir)
			diag_page = '/dermisroot/' + line2.split('"')[1]
			site2 = urllib2.urlopen(domain + diag_page)
			for line2 in site2:
				if '<img src="/bilder/' in line2:
					img_link = domain  + line2.split('"')[5]
					img_link = img_link.replace('100','550')
					print img_link
					img_id = img_link.split('/')[-1]
					if not os.path.isfile(img_dir+img_id): 
 						urllib.urlretrieve(img_link,img_dir+'/'+img_id)