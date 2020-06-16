import uuid
from django.db import models


# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField('Date of Birth', blank=True, null=True)
    NATIONS = (
        ('US', 'AMERICA'),
        ('VI', 'VIETNAM'),
        ('JP', 'JAPAN'),
        ('CN', 'CHINA'),
    )
    nation = models.CharField(max_length=2,
                              choices=NATIONS,
                              default='US')

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_detail_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def get_nation_display(self):
        return self.nation

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13, help_text='Enter 13 characters')

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    genre = models.ManyToManyField(Genre)

    class Meta:
        ordering = ['title']

    def get_detail_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    uuid = models.UUIDField('UUID',
                            primary_key=True,
                            default=uuid.uuid4,
                            help_text='Unique ID for this book instance')

    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('a', 'Available'),
        ('l', 'On loan'),
        ('r', 'Reserved')
    )

    status = models.CharField(max_length=1,
                              choices=LOAN_STATUS,
                              default='m',
                              help_text='Book availability')

    class Meta:
        ordering = ['due_back']

    def ge_status_display(self):
        return self.status[1]

    def __str__(self):
        return f'{self.uuid} {self.book.title}'
