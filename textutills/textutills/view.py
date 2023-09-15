# file is created by me
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
#return HttpResponse('Home')
def ex1(request):
    s='''
      <h1 align='center'>Navigation Port</h1>
      <a href='https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12' >Python Django playlist</a> <br>
      <a  href='https://economictimes.indiatimes.com/news'>Latest News</a><br>
      <a href='https://www.youtube.com/'>Youtube</a><br>
      <a href='https://www.google.com/'>Google</a>'''

    return HttpResponse(s)

def analyse(request):
    #get the text
    djtext=(request.POST.get('text','default'))
    removepunc=(request.POST.get('removepunc','off'))
    makecapital=(request.POST.get('makecapital','off'))
    extraspace_remover=(request.POST.get('extraspace_remover','off'))
    char_counter=(request.POST.get('char_counter','off'))
    #print(removepunc)
    #print(djtext)
    #analyse the text
    #analysed=djtext
    if makecapital=='on':
        analysed=""
        for char in djtext:
            analysed+=char.upper()
        params={'purpose':'Capitalize','analysed_text':analysed}
        djtext=analysed
        #return render(request,'analyse.html',params)

    if removepunc == 'on':
        analysed = ""
        punctuations='''!()-[];:'"\,<>./*?@#$5&^_~'''
        for char in djtext:
            if char not in punctuations:
                analysed += char
        params = {'purpose': 'Remove Punctuations', 'analysed_text': analysed}
        djtext=analysed
        #return render(request, 'analyse.html', params)

    if extraspace_remover=='on':
        analysed=""
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analysed+=char
        params={'purpose':'extra space remover','analysed_text':analysed}
        djtext=analysed
        #return render(request,'analyse.html',space_remover)

    if char_counter=='on':
        analysed=0
        for char in djtext:
            for i in char:
                if i==' ':
                    pass
                else:
                    analysed+=1
        params={'purpose':'char_counter','analysed_text':analysed}
        djtext=(analysed)
        #return render(request,'analyse.html',char_counter)

    if (makecapital!='on') and (removepunc != 'on') and (extraspace_remover!='on') and (char_counter!='on') :
        return HttpResponse('please select atleast one operation to perfom ')
    return render(request, 'analyse.html',params)




