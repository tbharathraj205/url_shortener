from django.shortcuts import render, redirect,get_object_or_404
from .models import shortURL
from django.http import HttpResponse
import secrets
import string


# Create your views here.


def home(request):
    obj = shortURL.objects.all()

    return render(
        request,
        'shortner/index.html',
        {'urls': obj}
    )

def create(request):
    if not request.method == 'POST':
        return redirect('shortner:home')
    
    
    original_url = request.POST.get('original_url')

    if not original_url:
        return render(
            request,
            'shortner/index.html',
            {'error':'Please enter an URL'}

        )
    
    characters = string.ascii_letters + string.digits
    short_url = ''.join(secrets.choice(characters) for _ in range(6))
    shortURL.objects.create(
        short_url= short_url,
        original_url=original_url
        )

    return render(
        request,
        'shortner/index.html',
        {
            'original_url': original_url,
            'short_url': short_url
        }
    )


def go(request, url=None):
    if not url:
        return HttpResponse('Invalid Path')

    obj = get_object_or_404(shortURL, short_url=url)

    return redirect(obj.original_url)

def list(request):

    url = {}

    obj = shortURL.objects.all()

    return render(request,'shortner/index.html',{'urls':obj})


    

    
