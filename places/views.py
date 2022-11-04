from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from django.urls import reverse

from .models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    context = {
        "title": place.title,
        'imgs': [item.image.url for item in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lon,
            'lat': place.lat
        }
    }
    return JsonResponse(context, safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})


def index(request):
    places = Place.objects.all()
    places_descriptions = []
    for place in places.iterator():
        place_description = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.lon, place.lat]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": reverse(get_place, args=[place.id])
                    }
                }
        places_descriptions.append(place_description)

    places_geojson = {
        "type": "FeatureCollection",
        "features": places_descriptions
        }
    return render(request, 'index.html', {"places_geojson": places_geojson})
