from django.contrib import admin

from electronics.models import TradeNetwork, Contact, Product


@admin.register(TradeNetwork)
class TradeNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'contact', 'products', 'supplier', 'debt', ]
    list_display_links = ['supplier']
    list_filter = ['contact__city']
    actions = ['clean_debt']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clean_debt(self, request, queryset):
        queryset.update(debt=0)


admin.site.register(Contact)
admin.site.register(Product)