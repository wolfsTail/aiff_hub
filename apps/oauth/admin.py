from django.contrib import admin

from .models import AuthUser, SocialLink


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'display_name','join_date')
    list_display_links = ('email',)
    list_filter = ('join_date',)


@admin.register(SocialLink)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'link')
