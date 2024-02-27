from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('image', 'username', 'password')}),
        ('Дополнительная информация', {'fields': ('first_name', 'last_name', 'email', 'bio', 'location', 'phone_number')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'image_tag')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f"<img src='{obj.image.url}' width='125px'>"
            )
        else:
            return f"Нет фотографии"