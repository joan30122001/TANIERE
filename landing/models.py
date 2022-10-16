from django.db import models








class Landing(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    

    class Meta:
        # db_table = 'category'
        verbose_name = "Landing"
        verbose_name_plural = "Landing"

    def __str__(self):
        return f'{self.first_name}'