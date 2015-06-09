from django.contrib import admin

# Register your models here.
from .models import Callreminders
from .models import Callunreachablelog
from .models import Clientmaster
from .models import Clientresponse
from .models import Clientresponsereasons
from .models import Reasonmaster
from .models import Terminationinitiationqueue

admin.site.register(Callreminders)
admin.site.register(Callunreachablelog)
admin.site.register(Clientmaster)
admin.site.register(Clientresponse)
admin.site.register(Clientresponsereasons)
admin.site.register(Reasonmaster)
admin.site.register(Terminationinitiationqueue)
