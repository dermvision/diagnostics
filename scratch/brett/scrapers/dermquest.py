import dryscrape, string, urllib, os

domain = 'https://www.dermquest.com'

page1 = dryscrape.Session(base_url=domain)
page1.visit('/image-library/image-search/')
for letter in string.ascii_uppercase:
    for diag in page1.xpath('//div[@id="diagnosis"]//div[@id="alpha-{}"]//li'.format(letter)):
        img_dir = diag.text()
        print img_dir
        if img_dir[0] in string.ascii_uppercase[:19]: continue
        if not os.path.exists(img_dir): os.makedirs(img_dir)
        diag_id = diag['data-facet-id']
        diag_page = '/image-library/image-search/#image-search/perPage=100000&diagnosis=' + diag_id
        page2 = dryscrape.Session(base_url=domain)
        page2.visit(diag_page)
        for img in page2.xpath('//img'):
 			if '/imagelibrary/' in img['src']:
 				img_id = img['src'].split('/')[3].split('?')[0]
 				img_link = domain + '/imagelibrary/large/' + img_id
 				print img_id
 				if not os.path.isfile(img_dir+img_id): 
 					urllib.urlretrieve(img_link,img_dir+'/'+img_id)