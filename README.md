# Dog API

Dog API - это веб-приложение, разработанное с использованием Django и Django REST Framework для управления данными о собаках и их породах. Это приложение предоставляет простой и понятный API для работы с информацией о собаках, включая их породы, характеристики и другую информацию.

## Установка и запуск проекта

Для установки и запуска проекта убедитесь, что у вас установлены Python, Docker и Docker Compose.

1. **Клонируйте репозиторий**:
```bash
   git clone &lt;url_вашего_репозитория&gt;
   cd имя_вашего_репозитория
```
2. **Создайте файл .env в корневой директории проекта и заполните его согласно примеру**

3. **Соберите контейнеры с помощью Docker Compose:**
```bash
   docker-compose up --build
```

#### Server будет запущен автоматически при сборке контейнеров.
#### Вы можете получить доступ к API по адресу: http://localhost:8000/api/.../.

## Архитектура проекта

Проект основан на архитектуре Django, включая следующие основные компоненты:

- **Модели**: Модели находятся в файле `models.py` и описывают структуру данных, такие как `Breed` (Порода) и `Dog` (Собака).
- **Сериализаторы**: Сериализаторы в файле `serializers.py` формируют структуры данных для отправки и получения через API.
- **Представления**: Представления в файле `views.py` обрабатывают запросы, взаимодействуют с моделями и возвращают сериализованные данные клиенту.
- **URLs**: Файл `urls.py` отвечает за маршрутизацию запросов к соответствующим представлениям.
- **Конфигурация приложения**: Файлы `settings.py` и `apps.py` содержат настройки и конфигурацию приложения.

## Примеры использования API
#### Получение списка пород собак:

```
Запрос: 
GET /api/breeds/

Ответ:
[
    {
        "name": "Лабрадор",
        "size": "Большая",
        "friendliness": 5,
        "trainability": 5,
        "shedding_amount": 3,
        "exercise_needs": 4,
        "dog_count": 5
    },
    {
        "name": "Бульдог",
        "size": "Средняя",
        "friendliness": 4,
        "trainability": 3,
        "shedding_amount": 2,
        "exercise_needs": 2,
        "dog_count": 2
    }
]
```

#### Создание новой собаки:
```
Запрос:
POST /api/dogs/

Тело запроса:
{
    "name": "Рекс",
    "age": 3,
    "breed": 1,
    "gender": "Мужчина",
    "color": "Черный",
    "favorite_food": "Курица",
    "favorite_toy": "Мяч"
}

Ответ:
{
    "id": 1,
    "name": "Рекс",
    "age": 3,
    "breed": 1,
    "gender": "Мужчина",
    "color": "Черный",
    "favorite_food": "Курица",
    "favorite_toy": "Мяч"
}