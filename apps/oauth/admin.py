from django.contrib import admin

from .models import AuthUser, SocialLink


@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username','join_date')
    list_display_links = ('email',)
    list_filter = ('join_date',)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'link')
