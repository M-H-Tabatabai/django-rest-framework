from django.contrib import admin
from bookshop.models import MyBook, Category, Author, BlockUserModel


# Register your models here.
@admin.register(MyBook)
class MyBookAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(BlockUserModel)
class AuthorAdmin(admin.ModelAdmin):
    pass
