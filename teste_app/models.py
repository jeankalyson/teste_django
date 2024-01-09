from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length = 200, default="texto")
    date_added = models.DateTimeField(auto_now_add=True)
    # método para mostrar o nome do tópico criado aqui 
    def __str__(self):
        return self.text
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    text = models.TextField( default="texto")
    date_added = models.DateTimeField(auto_now_add=True,null=True)
     
    class Meta:
        verbose_name_plural = 'entries'

    def __srt__(self):
        return self.text