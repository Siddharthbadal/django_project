from django.shortcuts import render
from django.http import HttpResponse
import random
import operator
# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    char = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        char.extend(list('.!@#$&^:/'))
    if request.GET.get('numbers'):
        char.extend(list("0123456789"))

    length = int(request.GET.get('length'))
    thepassword = ""
    for i in range(length):
        thepassword += random.choice(char)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')

def countpage(request):
    return render(request, 'generator/count.html')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()
	
	worddict = {}
	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1
	
	sortedwords= sorted(worddict.items(), key=operator.itemgetter(1), reverse = True)

	return render(request, 'generator/countresult.html',{'fulltext':fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})
