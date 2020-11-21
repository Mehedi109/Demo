from django.contrib import admin

from . models import teacher_top
from . models import teacher_bottom
from . models import course_top
from . models import course_bottom
from . models import contact_top
from . models import contact_bottom
from . models import contact_email
from . models import contact_call
from . models import Usermessage
from . models import about_top
from . models import description

admin.site.register(teacher_top)
admin.site.register(teacher_bottom)
admin.site.register(course_top)
admin.site.register(course_bottom)
admin.site.register(contact_top)
admin.site.register(contact_bottom)
admin.site.register(contact_email)
admin.site.register(contact_call)
admin.site.register(Usermessage)
admin.site.register(about_top)
admin.site.register(description)