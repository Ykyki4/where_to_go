from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Команда чтобы добавить новое место. Просто укажите адрес нужного json'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, nargs='+', help='Адрес нужного вам json.')

    def handle(self, *args, **options):
        try:
            for place_url in options['json_url']:
                place_response = requests.get(place_url)
                place_response.raise_for_status()
                place = place_response.json()
                image_urls = place['imgs']
                place_created, is_created = Place.objects.get_or_create(
                    title=place['title'],
                    lon=place['coordinates']['lng'],
                    lat=place['coordinates']['lat'],
                    defaults={
                        'description_short': place['description_short'],
                        'description_long': place['description_long'],
                    }
                )

                for order, img_url in enumerate(image_urls):
                    try:
                        filename = unquote(Path(urlparse(img_url).path).name)
                        image_response = requests.get(img_url)
                        image_response.raise_for_status()
                        image_content = ContentFile(image_response.content)

                        place_image = Image(order_numb=order, place=place_created)
                        place_image.image.save(filename, content=image_content)
                    except requests.exceptions.HTTPError:
                        self.stderr.write(self.style.ERROR(
                            f'Картинка по адресу {img_url} не найдена'))
        except requests.exceptions.HTTPError:
            self.stderr.write(self.style.ERROR(
                f'Описание локации по адресу {options["json_url"]} не найден'))