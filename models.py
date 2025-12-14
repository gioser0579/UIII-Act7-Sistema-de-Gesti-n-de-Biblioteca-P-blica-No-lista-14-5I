from django.db import models


# =========================
# Propietario
# =========================
class Propietario(models.Model):
    id_propietario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    fecha_registro = models.DateField()
    dni = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# =========================
# Mascota
# =========================
class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre_mascota = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE,
        related_name='mascotas'
    )
    chip_identificacion = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    esterilizado = models.BooleanField()

    def __str__(self):
        return self.nombre_mascota


# =========================
# Veterinario
# =========================
class Veterinario(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    licencia_veterinaria = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"


# =========================
# Consulta
# =========================
class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    fecha_consulta = models.DateTimeField()
    motivo_consulta = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    peso_mascota_consulta = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.TextField()

    def __str__(self):
        return f"Consulta {self.id_consulta}"


# =========================
# Vacuna
# =========================
class Vacuna(models.Model):
    id_vacuna = models.AutoField(primary_key=True)
    nombre_vacuna = models.CharField(max_length=100)
    descripcion = models.TextField()
    laboratorio = models.CharField(max_length=100)
    fecha_vencimiento_lote = models.DateField()
    tipo_enfermedad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_vacuna


# =========================
# Historial de Vacunación
# =========================
class HistorialVacunacion(models.Model):
    id_historial_vac = models.AutoField(primary_key=True)
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='historial_vacunacion'
    )
    vacuna = models.ForeignKey(
        Vacuna,
        on_delete=models.CASCADE,
        related_name='historial_vacunacion'
    )
    fecha_aplicacion = models.DateField()
    fecha_proxima_dosis = models.DateField()
    veterinario_aplico = models.ForeignKey(
        Veterinario,
        on_delete=models.CASCADE,
        related_name='vacunas_aplicadas'
    )
    numero_lote = models.CharField(max_length=50)
    comentarios = models.TextField()

    def __str__(self):
        return f"Vacunación {self.id_historial_vac}"


# =========================
# Factura Veterinaria
# =========================
class FacturaVeterinaria(models.Model):
    id_factura = models.AutoField(primary_key=True)
    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE,
        related_name='facturas'
    )
    fecha_emision = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    consulta_asociada = models.ForeignKey(
        Consulta,
        on_delete=models.CASCADE,
        related_name='facturas'
    )
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return f"Factura {self.id_factura}"

