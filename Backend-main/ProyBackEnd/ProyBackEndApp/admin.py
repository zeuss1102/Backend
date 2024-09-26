from django.contrib import admin
from .models import Post  # Asegúrate de importar el modelo que creaste

admin.site.register(Post)  # Registra el modelo en el panel de administración
