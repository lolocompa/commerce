from django.contrib import admin
from .models import listing
from .models import User
from .models import bid
from .models import comments

admin.site.register(listing)
admin.site.register(User)
admin.site.register(bid)
admin.site.register(comments)



# Register your models here.
