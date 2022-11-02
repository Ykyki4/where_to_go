from django.shortcuts import render
from .models import Place


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
                        "detailsUrl": "static/places/moscow_legends.json"
                    }
                }
        places_descriptions.append(place_description)

    places_geojson = {
        "type": "FeatureCollection",
        "features": places_descriptions
        }
    return render(request, 'index.html', {"places_geojson": places_geojson})

