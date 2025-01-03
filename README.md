# Веб-приложение для управления задачами

## Идея и концепция проекта
Главная идея — создать веб-приложение для управления задачами на основе фотографий. Продавцы загружают фотографии, операторы обрабатывают их и меняют статусы задач.

## Выбор базы данных
- **Разработка**: SQLite для удобства и быстроты.
- **Продакшн**: PostgreSQL для сложных запросов и транзакций.

## Архитектура приложения
- **Разработка**: Использование Bootstrap для простоты.
- **Продакшн**: Возможность использования JavaScript фреймворков, таких как React или Vue.js.

## Аутентификация и авторизация
- Логин и пароль, управление пользователями через Django Admin.

## Модели и структура данных
- **Task**: Модель для хранения информации о задачах.
- **User**: Стандартная модель пользователя Django с дополнительными ролями (оператор, магазин).

## API и взаимодействие с клиентом
- **POST /tasks**: Создание новой задачи.
- **GET /tasks**: Получение списка задач.
- **PATCH /tasks/{id}**: Обновление статуса задачи.

## Интерфейс пользователя
- **Главная страница**: Логин.
- **Страница создания задачи**: Для пользователей с ролью магазин.
- **Страница обработки задач**: Для операторов.
- **Список брака**: Для всех пользователей после логина.
- **Список закрытых задач**: Для операторов и магазинов после логина.

## Дополнительные функции
- **Журнал действий** (опционально).
- **Уведомления** (опционально).
- **Аналитика** (опционально).

## Дополнительные требования
- Лёгкая загрузка фотографий.
- Автоматический статус "Ожидает обработки".
- Возможность приблизить/отдалить и повернуть изображение.
- Статус "Брак фотографии" с уведомлением пользователю-отправителю.
