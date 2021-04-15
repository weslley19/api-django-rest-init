from django.db import models


class Base(models.Model):
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)


class Books(Base):
    name = models.CharField('Nome', max_length=100)
    author = models.CharField('Autor', max_length=255)
    pages = models.IntegerField('Quantidade de páginas')
    date_release = models.CharField('Data de lançamento', max_length=15, default='')

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
