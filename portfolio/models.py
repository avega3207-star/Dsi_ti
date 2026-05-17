from django.db import models

class portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(upload_to='portfolio', verbose_name='Imagen')
    link = models.URLField(null=True, blank=True ,verbose_name='Link (Opcional)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'portfolio'
        verbose_name = 'portfolio'
        verbose_name_plural = 'portfolios'

    def __str__(self):
        return self.title

