from django.db import models

# Create your models here.
class SearchResult(models.Model):
    keyword = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}({})'.format(self.keyword, self.search_date)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.URLField()
    release_date = models.DateField()
    search_result = models.ForeignKey(SearchResult, on_delete=models.CASCADE)

    def __str__(self):
        return '{}({})'.format(self.name, self.release_date)
