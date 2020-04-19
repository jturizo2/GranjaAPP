from django.contrib import admin
from apps.trans.models import serviInsu, TypeTrans, ClassTrans, transaction,ClassTransInsServ

# Register your models here.

admin.site.register(serviInsu)
admin.site.register(TypeTrans)
admin.site.register(ClassTrans)
admin.site.register(transaction)
admin.site.register(ClassTransInsServ)

