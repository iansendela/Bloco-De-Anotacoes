from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


class Tema(models.Model):
    tema = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tema
    


class BlocoNota(models.Model):
    titulo = models.CharField(max_length=255)
    assunto = models.CharField(max_length=255)
    tema = models.ForeignKey(Tema, related_name='tema_bloco' ,on_delete=models.CASCADE)
    conclusao = CKEditor5Field('Text', config_name='extends')
    data_criada = models.DateTimeField(auto_now_add=True)
    

    
    def __str__(self):
        return self.titulo
    
    
    class Meta:
        verbose_name = 'BlocoNota'
        verbose_name_plural = 'BlocosNotas'
        ordering = ['-data_criada']
        
        
    @property
    def days_ago(self):
        current_date = timezone.now()
        difference = current_date - self.data_criada
        return difference.days

    
    @property
    def hours_minutes_ago(self):
        current_date = timezone.now()
        difference = current_date - self.data_criada
        minutes, _ = divmod(difference.seconds, 60)
        if difference.days >= 1:
            return f"{difference.days} dias"
        elif difference.seconds >= 3600:
            return f"{difference.seconds // 3600} horas"
        else:
            return f"{minutes} minutos"
        
    @property 
    def fitro_temas(self):
        
        listas_temas = []
        
        temas = Tema.objects.all()
        
        for tem in temas:
            listas_temas.append(tem)
        
        
        # ainda não terminei
        return listas_temas
   
    
    

