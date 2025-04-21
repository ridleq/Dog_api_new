from rest_framework import serializers

from dog.models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализует модель Порода, включая информацию о породе собак
    и список собак, относящихся к данной породе.
    """
    dog_count = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = ('name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs', 'dog_count')

    def get_dog_count(self, obj):
        """
        Получает количество собак, связанных с породой указанной собаки.
        """
        return Dog.objects.filter(breed=obj).count()


class DogSerializer(serializers.ModelSerializer):
    """
    Сериализует модель Собака, включая информацию о породе собаки и
    вычисляемое поле для количества собак той же породы.
    """
    breed_info = BreedSerializer(source='breed', read_only=True)
    dog_count = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = (
            'name', 'age', 'breed', 'gender', 'color', 'favorite_food', 'favorite_toy', 'breed_info', 'dog_count'
        )

    def get_dog_count(self, obj):
        """
        Получает количество собак, связанных с породой указанной собаки.
        """
        return Dog.objects.filter(breed=obj.breed).count()
