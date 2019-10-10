from django.db import models
from django.conf import settings

class LikesDislikes(models.Model):
    count_likes = models.PositiveIntegerField()
    count_dislikes = models.PositiveIntegerField()

    def get_value(self):
        return self.count_likes - self.count_dislikes

class Post(LikesDislikes):
    text_content = models.TextField(blank=True, null=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posted_by', on_delete=models.CASCADE)
    count_comments = models.PositiveIntegerField(default=0)

    def children(self):
        return self.count_comments.filter(parent=None)

    def __str__(self):
        return self.text_content

class Comments(LikesDislikes):
    posted_comment = models.ForeignKey(Post, related_name='posted', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='author_comments', on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class SubGeddit(models.Model):
    name = models.CharField(max_length=150)
    posts = models.ManyToManyField('Post', related_name='subgeddit', blank=True)

    def __str__(self):
        return self.name

class SubGedditPost(models.Model):
    subgeddit = models.ForeignKey('SubGeddit', related_name='subgeddit_posts', on_delete=models.CASCADE)
    posts = models.ForeignKey('Post', related_name='subgeddit_p', on_delete=models.CASCADE)

    class Meta: unique_together = ['subgeddit', 'posts'] # so django will make a subgeddit and post uniquely identify a SubGedditpost object