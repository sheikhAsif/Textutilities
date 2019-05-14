__author__ = 'Asif Mohd Sheikh'

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    analyzed = ""
    #Get the text
    djtext = request.POST.get('textArea','default')  # if not get anything in textArea then set default
    # print(djtext) # prints on the terminal

    #check checkbox values
    removepunc = request.POST.get('removepunc','off')  #if anybody checked the checkbox then 'on' goes otherwise 'off'
    #print(removepunc)
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')
    numberremover = request.POST.get('numberremover','off')
    purpose = ""
    #check which checkbox is on
    if (removepunc == "on"):
        purpose = purpose+'|Removed Punctuations|-'
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #punctuation list getted from the internet
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        purpose = purpose+'|Full Capitalize|-'
        analyzed = ""
        analyzed = djtext.upper()
        print(purpose)
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        purpose = purpose+'|Extra space remover|-'
        analyzed = ""
        obj1 = enumerate(djtext)
        for index,char in obj1:
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                    analyzed += char
            else:
                pass
        params = {'purpose' :purpose , 'analyzed_text' : analyzed}
        djtext = analyzed
        print(analyzed)

    if (newlineremover == "on"):
        purpose = purpose +'|New Line Remover|-'
        analyzed = ""
        for char in djtext:
            if( char != "\n" and char != "\r"):
                analyzed += char
        params = {'purpose':purpose, 'analyzed_text':analyzed}
        djtext = analyzed

    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcounter == "on"):
        purpose = purpose + '|Char Counter|-'
        d = {}
        def count_char(text,char):
            count = 0
            for c in text:
                if c == char:
                    count += 1
            return count

        for c in djtext:
            count =  count_char(djtext,c)
            d[c] = count
        params = {'purpose': purpose,'analyzed_text':d}



    if(numberremover != "on" and charcounter != "on" and removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return render(request, 'error.html')


    return render(request, 'analyze.html', params)

