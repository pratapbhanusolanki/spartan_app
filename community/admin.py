from django.contrib import admin
from .models import User
from .models import Club
from .models import Event


admin.site.register(User)
admin.site.register(Club)
admin.site.register(Event)

