from django.contrib import admin

from .models import UsedPC
from .models import NewPC
from .models import Sp

admin.site.register(UsedPC)
admin.site.register(NewPC)
admin.site.register(Sp)

