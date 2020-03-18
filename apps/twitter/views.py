from django.shortcuts import render

def twitter(request):
    return render(request, 'feed.html', {})

