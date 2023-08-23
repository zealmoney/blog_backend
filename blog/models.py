from django.db import models

def author_upload_to(instance, filename):
    return 'author/{filename}'.format(filename=filename)

def upload_to(instance, filename):
    return 'post/{filename}'.format(filename=filename)

class Author(models.Model):
    name = models.CharField(max_length=200 , unique=True)
    photo = models.ImageField(upload_to=author_upload_to)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Categorie'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=400, unique=True)
    slug = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()
    featuredImage = models.ImageField(upload_to=upload_to)
    featuredPost = models.BooleanField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name')

    def __str__(self):
        return self.title    
    
class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    dateadded = models.DateTimeField(default='2023-04-10')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, to_field='title')

    def __str__(self):
        return self.comment
