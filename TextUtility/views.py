from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def removepunctuation(request):
    djtext = request.GET.get('text', 'default')
    RemovePunctuation = request.GET.get('RemovePunctuation', 'off')
    upperCase = request.GET.get('upperCase', 'off')
    newLine = request.GET.get('newLine','off')
    charCount = request.GET.get('charCount','off')
    print(RemovePunctuation)
    if RemovePunctuation == 'on':
     punctuation = '''". , ? ! : ; ' \" - – — ( ) [ ] { } ... / \\ ` ´ ~ ^ • · # & @ * _ |"'''
     analyzed = ""
     for char in djtext:
         if char not in punctuation:
            analyzed = analyzed + char
     params = {'purpose': 'RemovePunctuation', 'analyzed_text': analyzed}
     return render(request, 'analyze.html', params)
    elif upperCase == "on":
         upperText = djtext.upper()
         params = {'purpose': 'upCase', 'analyzed_text': upperText}
         return render(request, 'analyze.html', params)
    elif newLine == "on":
        analyzed = ""
        for char in djtext:

            if char !="/n":
             analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charCount == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")



def capitals(request):
   return HttpResponse("On capital page")
def newlineremover(request):
    return HttpResponse("Hello World")
def spaceremover(request):
    return HttpResponse('''Spece remover '<a href="/capitals" class="link-button">Go to capitals</a>''')


def charcount(request):
    return HttpResponse("Hello World")
