from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .models import shortURL
import secrets
import string
from django.views.decorators.csrf import csrf_exempt


def home(request):
    obj = shortURL.objects.all()

    urls = [
        {
            'short_url': item.short_url,
            'original_url': item.original_url,
        }
        for item in obj
    ]

    return JsonResponse({
        'urls': urls
    })

@csrf_exempt
def create(request):
    if request.method != 'POST':
        return JsonResponse(
            {'error': 'Only POST method is allowed'},
            status=405
        )

    original_url = request.POST.get('original_url')

    if not original_url:
        return JsonResponse(
            {'error': 'Please enter a URL'},
            status=400
        )

    characters = string.ascii_letters + string.digits

    # Generate a unique short URL
    while True:
        short_url = ''.join(
            secrets.choice(characters) for _ in range(6)
        )

        if not shortURL.objects.filter(short_url=short_url).exists():
            break

    obj = shortURL.objects.create(
        short_url=short_url,
        original_url=original_url
    )

    return JsonResponse({
        'message': 'Short URL created successfully',
        'original_url': obj.original_url,
        'short_url': obj.short_url,
    }, status=201)


def go(request, url=None):
    if not url:
        return JsonResponse(
            {'error': 'Invalid path'},
            status=400
        )

    obj = get_object_or_404(shortURL, short_url=url)

    return redirect(obj.original_url)


def list(request):
    obj = shortURL.objects.all()

    urls = [
        {
            'short_url': item.short_url,
            'original_url': item.original_url,
        }
        for item in obj
    ]

    return JsonResponse({
        'urls': urls
    })


def delete(request):
    if request.method != 'DELETE' and request.method != 'POST':
        return JsonResponse(
            {'error': 'Only DELETE or POST method is allowed'},
            status=405
        )

    # For POST requests
    url = request.POST.get('short_url')

    if not url:
        return JsonResponse(
            {'error': 'short_url is required'},
            status=400
        )

    obj = get_object_or_404(shortURL, short_url=url)

    obj.delete()

    return JsonResponse({
        'message': 'Short URL deleted successfully',
        'short_url': url
    })