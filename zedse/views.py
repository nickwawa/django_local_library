from django.shortcuts import render

def index(request):
    data = {
        'title': 'Home',
        'values': ['Son', 'Wtf', 'one'],
        'obj': {
            'Chevy': 'Hotline Miami',
            'dollars': '10,000',
            'owner': 'Страница отчасти посвящена'
        }
    }
    return render(request, 'zedse/index.html', data)

def about(request):
    return render(request, 'zedse/about.html')


def begin(request):
    return render(request, 'zedse/begin.html')

def frnds(request):
    return render(request, 'zedse/frnds.html')


