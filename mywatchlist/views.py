from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_html(request):
    # Men-assign data dengan semua data MyWatchList
    data = MyWatchList.objects.all()

    # Mencari jumlah film yang ditonton >= film yg belum ditonton
    data_watched_count = MyWatchList.objects.filter(watched="True").count()
    data_havent_watched_count = MyWatchList.objects.filter(watched="False").count()
    watched_a_lot = data_watched_count >= data_havent_watched_count
    context = {
        'list_mywatchlist': data,
        'watched_a_lot': watched_a_lot,
        'name': 'Airel Camilo Khairan',
        'id': '2106652581'
    }
    
    # Menggabungkan template dengan models
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")