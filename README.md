# Математический тест для 10 класса

Небольшое веб-приложение на Flask: четыре задания с вариантами ответов и итоговым количеством баллов.

## Структура

```text
app.py                 # Flask-маршруты и проверка ответов
templates/quiz.html    # Страница теста
templates/result.html  # Страница результата
static/style.css       # Оформление интерфейса
requirements.txt       # Зависимости Python
```

## Запуск на Windows

1. Откройте PowerShell в папке проекта.
2. Создайте виртуальное окружение:

   ```powershell
   python -m venv .venv
   ```

3. Активируйте его:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Установите зависимости:

   ```powershell
   pip install -r requirements.txt
   ```

5. Запустите приложение:

   ```powershell
   python app.py
   ```

6. Откройте в браузере адрес `http://127.0.0.1:5000`.

Чтобы остановить сервер, нажмите `Ctrl+C` в окне PowerShell.
