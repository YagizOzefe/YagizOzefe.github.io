from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    todo = models.CharField(max_length = 100) # Charfield =
    slug = AutoSlugField(populate_from= 'todo',unique = True) # Autoslug field bize populate from değerine girilen alanı döndürecektir. Unique = True ise her bir slugun özel isim olmasını sağlar
    user = models.ForeignKey(User,on_delete = models.CASCADE) # on_delete =  Silindiği zaman ilişkiyi bitir.
    # Foreign key bize ilişki kurmamızı sağlar. 
    def __str__(self):
        return self.todo
    
    
    


    