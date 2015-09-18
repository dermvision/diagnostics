import os, json
from string import join, lowercase, uppercase
from difflib import SequenceMatcher
from numpy import *

def sim(a, b):
	"""
	Computes match score between 0 and 1 for two strings
	"""
	score = SequenceMatcher(None, join(a, ''), join(b, '')).ratio()
	return score

def get_best_path(y, T, p=[]):
	"""
	Recursively finds the best path p of disease y in taxonomy T
	"""
	PS = [get_best_path(y, t, p+[t['name']]) for t in T['children']]
	ps = (p, sim(y, T['name']))
	PS.append(ps)
	p, s = PS[argmax([s for p, s in PS])]
	return p, s

def read_labels(f):
	"""
	Reads labels text file f into list of tuples D
	"""
	with open(f, 'rb') as file: D = file.readlines()
	D = [d.split('|') for d in D]
	D = [(x, clean(y)) for x, y in D]
	return D

def clean(k):
	"""
	Cleans string to standard format
	"""
	k = k.replace('-',' ').split()
	clean_string = lambda s: filter(lambda c: c in lowercase, s.lower())
	k = map(clean_string, k)
	k = filter(lambda s: len(s), k)
	return k

def print_match(disease, path, score):
	"""
	Prints the disease, taxonomy path, and match score
	"""
	disease_nice = join(disease)
	path_nice = join([join(i, '-') for i in path], '/')
	match_string = 'disease: {}'+'\n'+'path: {}'+'\n'+'score: {}'+'\n'
	match_string = match_string.format(disease_nice, path_nice, score)
	print match_string

def parse_rawdata(databases_root, databases, taxonomy_file):
	"""
	Given a list of databases and the taxonomy file, returns and saves the
	the list of tuples (image path, 
					    image label, 
						path in taxonomy, 
						match score)
	"""
	data = []

	pj = os.path.join
	ls = os.listdir

	taxonomy = json.load(open(taxonomy_file))

	for db in databases:
		db_data = read_labels(pj(databases_root, db, 'labels.txt'))
		images = ls(pj(databases_root, db, 'images'))
		for image, disease in db_data:
			if image in images:
				image_path = pj(databases_root, db, 'images', image)
				data.append((image_path, tuple(disease)))
		
	data = list(set(data))

	diseases = sorted({disease for image_path, disease in data})

	path_scores = []
	for disease in diseases:
		path_score = get_best_path(disease, taxonomy)
		path_scores.append(path_score)
		print_match(disease, *path_score)

	data = [(image_path, disease) + path_scores[diseases.index(disease)] 
			for image_path, disease in data]
	
	json.dump(data, open('data.json', 'w'))

	return data