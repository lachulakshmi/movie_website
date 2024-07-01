
#from django.contrib import admin
#from .models import Category
#from .models import Movie
#from .models import Category, Movie, Review
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

#admin.site.register(Category)
#admin.site.register(Movie)
#admin.site.register(Review)



# movies/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Category, Movie, Review

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'comment')
    search_fields = ('movie__title', 'user__username', 'comment')

# Custom UserAdmin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
