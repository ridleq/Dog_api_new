from django.db.models import Avg
from rest_framework import response, viewsets

from dog.models import Breed, Dog

from .serializers import BreedSerializer, DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с собаками.

    Позволяет выполнять стандартные операции CRUD (создание, чтение, обновление, удаление)
    над моделью Собака.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def list(self, request, *args, **kwargs):
        """
        Получает список пород и их средний возраст.

        В ответ возвращает данные по каждой породе с указанием имени породы
        и её среднего возраста.
        """
        breeds = Breed.objects.all()
        breed_data = []
        for breed in breeds:
            average_age = Dog.objects.filter(breed=breed).aggregate(Avg('age'))['age__avg'] or 0
            breed_data.append({
                "name": breed.name,
                "average_age": average_age
            })
        return response.Response(breed_data)

    def retrieve(self, request, *args, **kwargs):
        """
        Получает отдельный экземпляр собаки по его идентификатору.

        В ответ возвращает сериализованные данные запрашиваемой собаки.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(serializer.data)


class BreedViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с породами собак.

    Позволяет выполнять стандартные операции CRUD (создание, чтение, обновление, удаление)
    над моделью Порода.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def list(self, request, *args, **kwargs):
        """
        Получает список всех пород собак.

        В ответ возвращает сериализованные данные по всем породам.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)
