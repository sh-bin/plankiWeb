from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админка'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'country', 'region_area', 'city', 'address1',
                    'address2', 'index']
    fieldsets = (
        ('Основные', {'fields': (
            'username', 'first_name', 'last_name', 'email', 'phone', 'password', 'country', 'region_area', 'city',
            'address1', 'address2', 'index')}),
        ('Полномочия', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        ('Основные', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}),
    )
    list_display_links = ['username', 'email']
    search_fields = ['username', 'email', 'country', 'region_area', 'city', 'address1', 'address2', 'index']


@admin.register(CategorySlats)
class CategorySlatsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time_create']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Slats)
class SlatsAdmin(admin.ModelAdmin):
    fields = ['id', 'name', 'slug', 'description', 'category', 'image', 'get_image', 'stock', 'available', 'price',
              'time_create']
    readonly_fields = ['id', 'time_create', 'get_image']
    list_display = ['id', 'name', 'category', 'get_image', 'stock', 'available', 'price', 'time_create']
    list_display_links = ['id', 'name', 'get_image']
    list_editable = ['stock', 'available', 'price']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        else:
            return 'Фото не установлено'

    get_image.short_description = 'Миниатюра'