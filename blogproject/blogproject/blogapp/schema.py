import strawberry
from typing import List
from .models import BlogPost
from .types import BlogPostType


# Query
# GET or READ
@strawberry.type
class Query:
    @strawberry.field
    def blogposts(self, title: str = None) -> List[BlogPostType]:
        if title:
            blog = BlogPost.objects.filter(title=title)
            return blog
        return BlogPost.objects.all()

    @strawberry.field
    def blogpostsByLimit(self,limit: int=None) -> List[BlogPostType]:
        blogs = BlogPost.objects.all()[0:limit]
        return blogs

# Mutation
# Create, Update, Delete
# POST, PUT,PATCH, DELETE
@strawberry.type
class Mutation:
    @strawberry.field
    def create_blogpost(self, title: str, author: str, message: str) -> BlogPostType:
        blog = BlogPost(title=title, author=author, message=message)
        blog.save()
        return blog

    @strawberry.field
    def update_blogpost(self, id: int, title: str, author: str, message: str) -> BlogPostType:
        blog = BlogPost.objects.get(id=id)
        blog.title = title
        blog.author = author
        blog.message = message
        blog.save()
        return blog

    @strawberry.field
    def delete_blogpost(self,id: int) -> bool:
        blog = BlogPost.objects.get(id=id)
        blog.delete()
        return True

    # Define A Schema


schema = strawberry.Schema(query=Query, mutation=Mutation)
