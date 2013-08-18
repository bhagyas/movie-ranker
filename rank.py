import os
import json
import urllib2
import re
import sys

base_dir = "." #defaults to current folder
folders =  [name for name in os.listdir(base_dir) if os.path.isdir(name)]
zero_fill_length = len(str(len(folders))) + 1

#
# Disclaimer: 
#
# Whatever you do with this is your responsibility.
# By using this script you agree to use this only for good. 
# You shall not held the authors liable for any damages caused.
# Don't download movies illegally. It's bad.
# If you want to improve this, please fork the project, fix it and do a pull request.

# https://github.com/bhagyas/movie-ranker

def rank():
	request_url= "http://mymovieapi.com/?title={0}&type=json&plot=simple&episode=1&limit=1&yg=0&mt=none&lang=en-US&offset=&aka=simple&release=simple&business=0&tech=0"
	count = 0
	for folder in folders:
		rating = 10 #10 being the worst
		try:
			movie_result = json.load(urllib2.urlopen(request_url.format(folder)))
			rating = rating - movie_result[0]['rating']
			new_name = str(int(rating * 10)).zfill(zero_fill_length) + "_" + folder
			os.rename(os.path.join(base_dir, folder), os.path.join(".", new_name)) 
			print folder + " -> " + new_name
			count = count + 1
		except: 
			pass
	
	print "{0} movie folders ranked.".format(count)
			
def clear_rank():
	count = 0
	for folder in folders:
		try:
			if (int(folder[:zero_fill_length]) > 0 and folder[zero_fill_length] == '_'):			
				old_name = folder[zero_fill_length + 1:]
				os.rename(os.path.join(base_dir, folder), os.path.join(base_dir, old_name))
				print  folder + " -> " + old_name
				count = count + 1
		except:
			pass
	
	print "{0} movie folders reverted back to normal.".format(count)	

def main():
	if "--clear" in str(sys.argv):
		clear_rank()
	else:
		rank()
		
main()
