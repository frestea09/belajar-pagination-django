from django.shortcuts import render

def index(request):
    templateName = 'index.html'
    content = {
        'title':'Home',
        'article':'Selamat Datang diHome.',
        'dataFor':[
            ['/','Home'],
            ['/blog','Blog'],
        ]
    }
    return render(request,templateName,content)