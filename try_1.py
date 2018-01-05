
######-11-ud120:lesson12-4-######
"""
fraction = 0.
if (poi_messages !="NaN") or (all_messages !="NaN") :
    fraction = float(poi_messages)/all_messages
else :
    fraction = 0.
return fraction
"""

######-10-ud120:lesson12-3-######
"""
if from_emails:
        ctr = 0
        while not from_poi and ctr < len(from_emails):
            if from_emails[ctr] in poi_email_list:
                from_poi = True
            ctr += 1
"""

######-9-ud120:lesson11-19-#######
"""
data = []
for name, from_person in [("sara", 1), ("chris", 2)]:
	# print name,from_person
	if name == "sara":
		data.append(from_person)
	elif name == "chris":
		data.append(from_person)
print data
"""
"""
a = [1,2,3]
b = [9,6,1]
for i,j in zip(a,b):
	print i+j
"""	
######-8-ud120:lesson11-19-#######
"""
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
Str = " I am a good response responsitivity person"
print Str
"""
"""
Str = Str.replace("good","")
print Str
Str = ' '.join(Str.split())
print Str
"""
"""
Str = Str.replace("good ","")
print Str
Str = Str.replace("am ","").replace("a ","")
print Str
"""

######-7-ud120:lesson11-18-#######
"""
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
Str = " I am a good response responsitivity person"
print Str
# for x in Str.split( ):
	# print x
singles = [stemmer.stem(word) for word in Str.split( )]
print singles
st = ' '.join(singles)
print st
"""

######-6-ud120:lesson10-#######
"""
from nltk.corpus import stopwords
sw = stopwords.words("english")
print len(sw)

# import nltk
# nltk.download('stopwords')
"""
