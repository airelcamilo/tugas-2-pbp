from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    # Men-assign data_katalog dengan semua data CatalogItem
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_katalog,
        'name': 'Airel Camilo Khairan',
        'id': '2106652581'
    }
    
    # Menggabungkan template dengan models
    return render(request, "katalog.html", context)