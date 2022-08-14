from django.db import models



class GonderiModel(models.Model):
    yazar=models.ForeignKey("auth.user",on_delete=models.CASCADE)
    baslik=models.CharField(max_length=200)
    yazi=models.TextField()
    
    
    yayimzaman=models.DateTimeField(blank=True,null=True)
    #blank vebsayfası üzerinde boş geçilemez,null=> veritabanı üzerinde boşgeçilemez,blank true null false OLAMAZ
    e_posta=models.EmailField(blank=True,null=True)
    
    
    def __str__(self) :
        return self.baslik
    
        
