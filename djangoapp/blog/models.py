from django.db import models
from utils.rands import slugify_new

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique= True, default= None,
        null= True, blank= True, max_length=255,
    )

    def save(self, *args, **Kwargs):
        if not self.slug:
            self.alug = slugify_new(self.name)
        return super().save(*args, **Kwargs)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique= True, default= None,
        null= True, blank= True, max_length=255,
    )

    def save(self, *args, **Kwargs):
        if not self.slug:
            self.alug = slugify_new(self.name)
        return super().save(*args, **Kwargs)

    def __str__(self):
            return self.name

class Page(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique= True, default= None,
        null= True, blank= True, max_length=255,
    )
    is_published = models.BooleanField(
         default=False,
         help_text=('Este campo deve ser marcado' 
                    'para a página ser exibida publicamente'
         ),
    )
    content =  models.TextField()

    def save(self, *args, **Kwargs):
        if not self.slug:
            self.alug = slugify_new(self.title)
        return super().save(*args, **Kwargs)

    def __str__(self):
            return self.title
