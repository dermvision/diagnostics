import urllib, os
domain = 'http://www.dermnet.com'
site = urllib.urlopen(domain+'/dermatology-pictures-skin-disease-pictures/').readlines()
for line in site:
	if '<a href=' in line:
		link = line.split('"')[1]
		if '/images/' in link:
			site2 = urllib.urlopen(domain+link).readlines()
			for line2 in site2:
				if '<a href=' in line2:
					link2 = line2.split('"')[1]
					if '/images/' in link2:
						imdir = link.split('/')[2] + '/' + link2.split('/')[2] + '/'
						if not os.path.exists(imdir): os.makedirs(imdir)
						site3 = urllib.urlopen(domain+link2).readlines()
						num = 1
						for line3 in site3:
							if '<div class="pagination">' in line3:
								num = line3.split('<a href=')[-2]
								num = int(num.split('>')[1].split('<')[0])
						for i in range(num):
							site4 = urllib.urlopen(domain+link2+'/photos/'+str(i+1))
							for line4 in site4:
								if '<div class=desc>' in line4:
									img = line4.split('<div class=desc>')[-1].split('</div')[0]
									imglink = domain + '/dn2/allJPG3/' + img
									print imdir+img
									if not os.path.isfile(imdir+img): 
										urllib.urlretrieve(imglink,imdir+img)
