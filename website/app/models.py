from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    cat_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return "{}-{}".format(str(self.category),str(self.sub_category))
