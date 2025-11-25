from django.db import models

class AutorBiblioteca(models.Model):
    nombre_autor = models.CharField(max_length=100)
    apellido_autor = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()
    libros_destacados = models.TextField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_autor} {self.apellido_autor}"


class EditorialBiblioteca(models.Model):
    nombre_editorial = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    sitio_web = models.CharField(max_length=255)
    fecha_fundacion = models.DateField()

    def __str__(self):
        return self.nombre_editorial


class LibroBiblioteca(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(AutorBiblioteca, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    editorial = models.ForeignKey(EditorialBiblioteca, to_field='nombre_editorial', on_delete=models.CASCADE)
    anio_publicacion = models.IntegerField()
    genero = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
    num_ejemplares = models.IntegerField()
    fecha_adquisicion = models.DateField()
    estanteria = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    fecha_vencimiento_membresia = models.DateField()
    dni = models.CharField(max_length=20)
    tipo_socio = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Bibliotecario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    turno = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Prestamo(models.Model):
    libro = models.ForeignKey(LibroBiblioteca, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion_esperada = models.DateField()
    fecha_devolucion_real = models.DateTimeField(null=True, blank=True)
    estado_prestamo = models.CharField(max_length=50)
    multa_generada = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bibliotecario = models.ForeignKey(Bibliotecario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Préstamo {self.id}"


class Multa(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    monto_multa = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_generacion = models.DateTimeField()
    fecha_pago = models.DateTimeField(null=True, blank=True)
    estado_pago = models.CharField(max_length=50)
    motivo_multa = models.TextField()
    socio_multado = models.ForeignKey(Socio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Multa {self.id}"
