from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def removepunctuation(request):
    djtext = request.POST.get('text', 'default')
    RemovePunctuation = request.POST.get('RemovePunctuation', 'off')
    upperCase = request.POST.get('upperCase', 'off')
    newLine = request.POST.get('newLine','off')
    charCount = request.POST.get('charCount','off')
    print(RemovePunctuation)
    if RemovePunctuation == 'on':
     punctuation = '''". , ? ! : ; ' \" - – — ( ) [ ] { } ... / \\ ` ´ ~ ^ • · # & @ * _ |"'''
     analyzed = ""
     for char in djtext:
         if char not in punctuation:
            analyzed = analyzed + char
     params = {'purpose': 'RemovePunctuation', 'analyzed_text': analyzed}
     djtext = analyzed
    # return render(request, 'analyze.html', params)
    if upperCase == "on":
         upperText = djtext.upper()
         params = {'purpose': 'upCase', 'analyzed_text': upperText}
         djtext = analyzed
         #return render(request, 'analyze.html', params)
    if newLine == "on":
        analyzed = ""
        for char in djtext:

            if char !="/n" and char !="/r":
             analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if charCount == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        #djtext = analyzed

            #if(newLine !='on'and RemovePunctuation !='on' and upperCase != 'on'):
            #return HttpResponse('Choose any operation first')



    return render(request, 'analyze.html', params)



def capitals(request):
   return HttpResponse("On capital page")
def newlineremover(request):
    return HttpResponse("Hello World")
def spaceremover(request):
    return HttpResponse('''Spece remover '<a href="/capitals" class="link-button">Go to capitals</a>''')


def charcount(request):
    return HttpResponse("Hello World")
