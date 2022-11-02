from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    description_short = models.CharField("Короткое описание", max_length=350)
    description_long = models.TextField("Длинное описание")

    lat = models.FloatField(
        verbose_name='Широта',
        validators=[
            MinValueValidator(-90.0),
            MaxValueValidator(90.0)
        ]
    )

    lon = models.FloatField(
        verbose_name='Долгота',
        validators=[
            MinValueValidator(-180.0),
            MaxValueValidator(180.0)
        ]
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    order_numb = models.SmallIntegerField("Порядок", default=0)
    image = models.ImageField("Картинка")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"{self.order_numb} {self.place.title}"

    class Meta(object):
        ordering = ['order_numb']
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
