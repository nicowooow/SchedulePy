# 1. Imagen base ligera de Python
FROM python:3.13-slim

# 2. Evitar que Python guarde .pyc y que haga buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Crear carpeta de trabajo
WORKDIR /app

# 4. Instalar dependencias del sistema (si las necesitas)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copiar requirements e instalarlos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar el código del proyecto dentro del contenedor
COPY . /app/

# 7. Exponer el puerto interno donde correrá Django
EXPOSE 8000

# 8. Comando por defecto: Gunicorn con tu proyecto Django
CMD ["gunicorn", "practica_despliegue.wsgi:application", "--bind", "0.0.0.0:8000"]
