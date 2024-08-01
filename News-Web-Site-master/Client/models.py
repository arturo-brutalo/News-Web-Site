from django.db import models

class News(models.Model):
    header = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='static/', null=False, blank=False)
    alternative_text = models.CharField(max_length=100, null=False, blank=False, default='image')
    publish_date = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
        return f'Header: {self.header}, publish date: {self.publish_date}, description: {self.description[:100]}'
        
    class Meta:
        verbose_name_plural = 'News' 