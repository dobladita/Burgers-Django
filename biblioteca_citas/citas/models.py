from django.db import models

# Create your models here.
from django.db import models

# Modelo Fuente
class Fuente(models.Model):
    nombre = models.CharField(max_length=200, help_text="Nombre de la fuente (por ejemplo, 'Libro A', 'Artículo B')")
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('libro', 'Libro'),
            ('articulo', 'Artículo'),
            ('discurso', 'Discurso'),
            ('otro', 'Otro')
        ],
        help_text="Tipo de fuente: libro, artículo, discurso, etc."
    )

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

# Modelo Cita
class Cita(models.Model):
    texto = models.TextField(help_text="El texto de la cita.")
    autor = models.CharField(max_length=100, help_text="Nombre del autor de la cita (por ejemplo, 'William Shakespeare')")
    fecha = models.DateField(null=True, blank=True, help_text="Fecha aproximada de la cita, si está disponible")
    fuente = models.ForeignKey(Fuente, on_delete=models.CASCADE, related_name='citas', help_text="Fuente de la cita")

    def __str__(self):
        return f"{self.autor}: {self.texto[:50]}..."
