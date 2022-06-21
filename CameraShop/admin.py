from django.contrib import admin

# Register your models here.
from CameraShop.models import *
from CameraShop.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('productFrontImage_preview', 'productBackImage_preview', 'photo1_preview', 'photo2_preview')

    def productFrontImage_preview(self, obj):
        return obj.productFrontImage_preview

    productFrontImage_preview.short_description = 'FrontImage_preview'
    productFrontImage_preview.allow_tags = True

    def productBackImage_preview(self, obj):
        return obj.productBackImage_preview

    productBackImage_preview.short_description = 'BackImage_preview'
    productBackImage_preview.allow_tags = True

    def photo1_preview(self, obj):
        return obj.photo1_preview

    photo1_preview.short_description = 'Photo1_preview'
    photo1_preview.allow_tags = True

    def photo2_preview(self, obj):
        return obj.photo2_preview

    photo2_preview.short_description = 'Photo2_preview'
    photo2_preview.allow_tags = True


admin.site.register(Company)
admin.site.register(Image, ImageAdmin)
admin.site.register(ISOSpeed)
admin.site.register(ShutterSpeed)
admin.site.register(Sensor)
admin.site.register(LensMount)
admin.site.register(Aperture)
admin.site.register(LensFormat)
admin.site.register(Color)
admin.site.register(Camera)
admin.site.register(FocalLength)
admin.site.register(Lens)
admin.site.register(User)
admin.site.register(CameraBill)
admin.site.register(LenBill)
admin.site.register(Bill)
admin.site.register(Order)