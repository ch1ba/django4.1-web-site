from django.db import models
from django.urls import reverse


class Simple(models.Model):
    title = models.CharField(max_length=100,verbose_name="Заголовок")
    content = models.TextField(blank=True,verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True,verbose_name="Время последнего обновления")
    is_published = models.BooleanField(default=True,verbose_name="Опубликовано")
    cat = models.ForeignKey("Category",on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Category(models.Model):
    name = models.CharField(max_length=20,db_index=True,verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_id": self.pk})





