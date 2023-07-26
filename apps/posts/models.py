from django.db import models
from apps.users.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=35)
    slug = models.SlugField(verbose_name='Понятный для', max_length=255, unique=True)
    
    def __str__(self):
        return self.name
        
class Movie(models.Model):
    title = models.CharField('Название фильма', max_length=200)
    description = models.CharField('Описание фильма',max_length=500)
    poster = models.ImageField('Постер фильма',upload_to="movie_poster/")
    trailer  = models.URLField('Трейлер')
    movie = models.FileField('Посмотреть фильм',upload_to='movie_video/')
    year = models.DateField("Дата выпуска", default=0)
    running_time = models.CharField('Длительность фильма', max_length=10)
    country = models.CharField("Страна",max_length=200)
    category = models.ForeignKey(Category,verbose_name = 'Категории',  on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,verbose_name = 'Пользователь',  on_delete=models.SET_NULL, null=True)
    directors = models.CharField("Режиссёры", max_length=555)
    actors = models.CharField("Актёры", max_length=50000, null=True, blank=True)
    genres = models.CharField('Жанры', max_length=255)
    rating = models.FloatField(default=10)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        
class Comment(models.Model):
    text = models.CharField(
        max_length=550
    )
    parent = models.ForeignKey(
        'self',
        related_name = 'child_comm',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    from_user = models.ForeignKey(
        User,
        related_name='comments_user',
        on_delete=models.CASCADE
    )
    to_post = models.ForeignKey(
        Movie,
        related_name='comments',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.text[:10]} - {self.from_user.username}"
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарийи'
        
class Like(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='liked_users',
        on_delete=models.CASCADE
    )
    to_post = models.ForeignKey(
        Movie,
        related_name='liked_posts',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.to_post.liked_posts.count}-{self.to_post.id}"
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        
class LikeComments(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='liked_comments',
        on_delete=models.CASCADE
    )
    to_comment = models.ForeignKey(
        Comment,
        related_name='liked_comments',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.to_comment.liked_comments.count}-{self.to_comment.id}"
    
    class Meta:
        verbose_name = 'Лайк для коммента '
        verbose_name_plural = 'Лайки для комментарий'