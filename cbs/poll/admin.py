from django.contrib import admin
from .models import Promise,Representative,PromiseGroup,Board
# Register your models here.


# class ClubInline(admin.TabularInline):
# 	model = Club
class PromiseInline(admin.StackedInline):
	model = Promise
class PromiseGroupsInline(admin.TabularInline):
	model = PromiseGroup

# class BoardAdmin(admin.ModelAdmin):
# 	inlines = [ClubInline,]	
class RepresentativeAdmin(admin.ModelAdmin):
	inlines = [PromiseGroupsInline,PromiseInline,]	
# admin.site.register(Promise)
# admin.site.register(PromiseGroup)
admin.site.register(Board)
# admin.site.register(Club)
admin.site.register(Representative,RepresentativeAdmin)
