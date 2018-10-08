from django.contrib import admin
from .models import Question
admin.site.register(Question)
from .models import Article
admin.site.register(Article)
