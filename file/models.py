from django.db import models


class UploadedFile(models.Model):
    title = models.CharField("Название файла", max_length=50)
    file = models.FileField('Файл', upload_to='uploads')
    upload_date = models.DateTimeField('', auto_now_add=True)
    file_size = models.CharField(max_length=50)
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
