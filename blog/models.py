from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
    id = models.AutoField(primary_key = True)
    fecha_add = models.DateField('Fecha de Creación',auto_now = False, auto_now_add = True)
    fecha_edit = models.DateField('Fecha de Modificación',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class Categoria(ModeloBase):
    categoria = models.CharField('Nombre de la Categoría', max_length = 100, unique = True)
    image_categoria = models.ImageField('Imagen Categoría',upload_to = 'categoria/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.categoria

class Post(ModeloBase):
    titulo = models.CharField('Título del Post',max_length = 150, unique = True)
    meta = models.CharField('Meta', max_length = 150, unique = True)
    descripcion = models.TextField('Descripción')
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    contenido = RichTextField()
    imagen_post = models.ImageField('Imagen Referencial', upload_to = 'imagenes/', max_length = 255)
    publicado = models.BooleanField('Publicado / No Publicado', default = False)
    fecha_publicacion = models.DateField('Fecha de Publicación', auto_now = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class Info(ModeloBase):
    nombre = models.CharField('Nombre del Blog', max_length = 50)
    titulo = models.CharField('Título del Blog', max_length = 100)
    subtitulo = models.CharField('Subtítulo del Blog', max_length = 100)
    nosotros = RichTextField()
    telefono = models.CharField('Teléfono', max_length = 10)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    direccion = models.CharField('Dirección', max_length = 200)
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Información'

    def __str__(self):
        return self.nombre


class Contacto(ModeloBase):
    nombres = models.CharField('Nombre', max_length = 100)
    apellidos = models.CharField('Apellidos', max_length = 150)
    correo = models.EmailField('Correo Electrónico', max_length = 200)
    asunto = models.CharField('Asunto', max_length = 100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto
