from django.contrib import admin

from .models import Breed, Dog


class DogAdmin(admin.ModelAdmin):
    """
    Администраторская панель для модели 'Собака'.

    Этот класс определяет настройки администрирования для модели Собака,
    включая поля, отображаемые в списке, поля для поиска и фильтрации.
    """
    list_display = ('name', 'age', 'breed', 'gender')
    search_fields = ('name', 'breed')
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class BreedAdmin(admin.ModelAdmin):
    """
    Администраторская панель для модели 'Порода'.

    Этот класс определяет настройки администрирования для модели Порода,
    включая поля, отображаемые в списке, поля для поиска и фильтрации.
    """
    list_display = (
        'name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs'
    )
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)
