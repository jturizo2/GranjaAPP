from django.contrib import admin
from apps.trans.models import *

# Register your models here.

admin.site.register(serviInsu)
admin.site.register(TypeTrans)
admin.site.register(ClassTrans)
admin.site.register(transaction)
admin.site.register(ClassTransInsServ)
admin.site.register(TypeTransserviInsu)
admin.site.register(transactionserviInsu)

