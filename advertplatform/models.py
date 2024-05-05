from django.db import models

class Seller(models.Model):
    seller_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, db_index=True)
    seller_type = models.CharField(max_length=255)
    date_first_added = models.DateField(auto_now_add=True)
    ad_platform = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
