from django.contrib import admin
from .models import Person, PersonDetail, PersonsImage, Event, EventDetail, EventImage, Food, FoodDetail, FoodImage, Clothe, ClotheDetail, ClotheImage

# Register your models here.
admin.site.register(Person)
admin.site.register(PersonDetail)
admin.site.register(PersonsImage)
admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(EventImage)
admin.site.register(Food)
admin.site.register(FoodDetail)
admin.site.register(FoodImage)
admin.site.register(Clothe)
admin.site.register(ClotheDetail)
admin.site.register(ClotheImage)