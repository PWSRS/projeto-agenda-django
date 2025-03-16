from django.contrib import admin

from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','email','created_date',
    ordering = '-id',
    # list_filter cria um filtro na página
    #list_filter = 'created_date',
    search_fields = 'first_name','email',
    list_per_page = 10
    list_max_show_all = 100
    #cria um input para poder editar os contatos
    #list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'first_name'

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
