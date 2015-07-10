import urllib2, os, string, urllib
domain = 'http://www.hellenicdermatlas.com'
site = urllib2.urlopen(domain+'/en/search/browse/').readlines()
for line in site:
	for line in line.split('<a href='):
		if '/en/' in line and '</a></li><li>' in line:
			img_dir = line.split('\'')[1].split('/')[2]
			if not os.path.exists(img_dir): os.makedirs(img_dir)
			print img_dir
			try:
				site2 = urllib2.urlopen(domain + '/en/' + img_dir + '/1/')
				num_pages=1;
				for line2 in site2:
					if 'pager' in line2:
						for line3 in line2.split(img_dir):
							if '</a> <a id=\'pager\'' in line3:
								try:
									num_pages = max(num_pages, int(line3.split('/')[1]))
								except:
									pass
				print num_pages
				for i in range(num_pages):
					site2 = urllib2.urlopen(domain + '/en/' + img_dir + '/' + str(i) + '/')
					for line2 in site2:
						if 'thumb.jpg' in line2:
							img_link = line2.split('src=')[1].split('\'')[1]
							img_link = img_link.replace('thumb', 'standalone')
							img_link = domain + img_link
							img_id = img_link.split('/')[-1].split('_')[0]+'.jpg'
							print img_link
							if not os.path.isfile(img_dir+img_id): 
 								urllib.urlretrieve(img_link,img_dir+'/'+img_id)
			except:
				pass