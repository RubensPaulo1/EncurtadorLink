from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Link
from django.urls import reverse

def index(request):
    if request.method == 'POST':
        original_url = request.POST.get('url')
        try:
            # Validar a URL
            validator = URLValidator()
            validator(original_url)
            
            link = Link.objects.create(original_url=original_url)
            short_url = request.build_absolute_uri(reverse('redirect', args=[link.short_code]))
            return render(request, 'shortener/index.html', {'short_url': short_url})
        except ValidationError:
            return render(request, 'shortener/index.html', {'error': 'URL inválida'})
    return render(request, 'shortener/index.html')

def redirect_to_url(request, short_code):
    link = get_object_or_404(Link, short_code=short_code)
    return redirect(link.original_url)
