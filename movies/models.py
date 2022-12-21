from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Avg
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Movies(models.Model):
    """    Фильмы    """
    title = models.CharField(max_length=255, verbose_name="Название фильма")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    plot = models.TextField(blank=True, verbose_name="Сюжет")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def average_rating(self) -> float:
        return RatingMovie.objects.filter(movie=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.title}: {self.average_rating()}"

    def get_absolute_url(self):
        return reverse('detail_movie', kwargs={'movie_slug': self.slug})

    class Meta:
        verbose_name = "Фильмы"
        verbose_name_plural = "Фильмы"
        ordering = ['?']


class Staff(models.Model):
    """    Персонал: актеры, режиссеры    """
    name = models.CharField(max_length=255, verbose_name="Имя фамилия")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    bio = models.TextField(blank=True, verbose_name="Сюжет")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    movies = models.ManyToManyField('Movies')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('staff', kwargs={'staff_slug': self.slug})

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"
        ordering = ['?']


class Category(models.Model):
    """    Категории пока только фильмов    """
    title_cat = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title_cat

    def get_absolute_url(self):
        return reverse('movies_by_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
        ordering = ['?']


class Profile(models.Model):
    """    Создаваемая пользователем страница профиля    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Фамилия")
    email = models.EmailField(max_length=255, unique=True, null=True)
    bio = models.TextField(max_length=2055, null=True, blank=True, verbose_name="О себе")
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/", verbose_name="Картинка профиля")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    """Комментарии к фильму"""
    movies = models.ForeignKey(Movies, related_name="comments", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Заголовок комментария")
    body = models.TextField(max_length=2550, verbose_name="Текст комментария")
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name='автор')

    def __str__(self):
        return '%s - %s' % (self.movies.title, self.title)


class RatingMovie(models.Model):
    """Рейтинг фильмов"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name="фильм")
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.movie.title}: {self.rating}"

    class Meta:
        verbose_name = "Рейтинг фильма"
        verbose_name_plural = "Рейтинги фильма"




