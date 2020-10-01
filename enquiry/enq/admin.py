from django.contrib import admin
from enq.models import *
# Register your models here.

admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Enquiry)
admin.site.register(Admission)
admin.site.register(Payment)