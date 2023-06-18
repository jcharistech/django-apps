import strawberry
from typing import List
from . import models


@strawberry.django.type(models.BlogPost)
class BlogPostType:
    id: int
    title: str
    author: str
    message: str
