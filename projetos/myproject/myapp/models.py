from django.db import models


class Books (models.Model):
    id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=50)

    author = models.CharField(max_length = 50)

    release_year = models.IntegerField()

    create_at = models.DateField(auto_now_add= True)
    RASCUNHO = 'ras'
    PRODUCAO = 'pro'
    PUBLICADA = 'pub'
    STATUS_CHOICES = (
        (RASCUNHO, 'rascunho'),
        (PRODUCAO, 'produzindo'),
        (PUBLICADA, 'publicada'),
	)

