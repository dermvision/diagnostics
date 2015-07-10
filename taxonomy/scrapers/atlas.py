import urllib2, os, string, urllib
domain = 'http://www.atlasdermatologico.com.br'

for diseaseID in range(501):
	site = urllib2.urlopen(domain+'/disease.jsf?diseaseId='+str(diseaseID+1)).readlines()
	for line in site:
		if '<span class="capitalized">' in line:
			img_dir = line.split('<span class="capitalized">')[1].split('<')[0]
			print img_dir
			if img_dir is '': continue
			if not os.path.exists(img_dir):
				os.makedirs(img_dir)
		if '?imageId=' in line:
			for img_id in line.split('?imageId='):
				if '&amp' in img_id:
					img_id = img_id.split('&amp')[0]
					img_link = 'http://www.atlasdermatologico.com.br/img?imageId=' + img_id
					print img_link
					if not os.path.isfile(img_dir+img_id): 
 						urllib.urlretrieve(img_link,img_dir+'/'+img_id)