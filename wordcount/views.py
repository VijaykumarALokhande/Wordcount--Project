from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    s = request.GET['fulltext']
    doc = s.split()
    oxford = {}
    for word in doc:
        if word in oxford:
            oxford[word]+=1
        else:
            oxford[word]=1
    return render(request, 'count.html', {'docx':oxford, 'length':len(doc)})

def about(request):
    return render(request, 'about.html')
