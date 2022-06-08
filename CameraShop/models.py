from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.html import mark_safe
from django.templatetags.static import static
import locale

# Create your models here.


class Company(models.Model):
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.companyName


class Image(models.Model):
    name = models.CharField(max_length=100, null=True)
    productFrontImage = models.ImageField(upload_to='CameraShop/static/CameraShop/img/save')
    productBackImage = models.ImageField(upload_to='CameraShop/static/CameraShop/img/save')
    photo1 = models.ImageField(upload_to='CameraShop/static/CameraShop/img/save')
    photo2 = models.ImageField(upload_to='CameraShop/static/CameraShop/img/save')

    @property
    def productFrontImage_preview(self):
        if self.productFrontImage:
            url = static(str(self.productFrontImage.url).replace("CameraShop/static/", ""))
            return mark_safe('<img src="{}"  height="300" />'.format(url))
        return ""

    @property
    def productBackImage_preview(self):
        if self.productBackImage:
            url = static(str(self.productBackImage.url).replace("CameraShop/static/", ""))
            return mark_safe('<img src="{}"  height="300" />'.format(url))
        return ""

    @property
    def photo1_preview(self):
        if self.photo1:
            url = static(str(self.photo1.url).replace("CameraShop/static/", ""))
            return mark_safe('<img src="{}"  height="300" />'.format(url))
        return ""

    @property
    def photo2_preview(self):
        if self.photo2:
            url = static(str(self.photo2.url).replace("CameraShop/static/", ""))
            return mark_safe('<img src="{}"  height="300" />'.format(url))
        return ""

    def __str__(self):
        return self.name


class ISOSpeed(models.Model):
    fromSpeed = models.IntegerField()
    toSpeed = models.IntegerField()

    def __str__(self):
        return self.fromSpeed.__str__() + "-" + self.toSpeed.__str__()


class ShutterSpeed(models.Model):
    fromSpeed = models.IntegerField()
    toSpeed = models.IntegerField()

    def __str__(self):
        return self.fromSpeed.__str__() + "-" + self.toSpeed.__str__()


class Sensor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LensMount(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Aperture(models.Model):
    minApertureType = models.CharField(max_length=100)
    maxApertureType = models.CharField(max_length=100)

    def __str__(self):
        return self.minApertureType + '-' + self.maxApertureType


class LensFormat(models.Model):
    lensTypeFormat = models.CharField(max_length=100)

    def __str__(self):
        return self.lensTypeFormat


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Camera(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color, verbose_name="list of color")
    description = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    price = models.FloatField(validators=[MinValueValidator(100000), MaxValueValidator(100000000)])
    isoSpeed = models.ForeignKey(ISOSpeed, on_delete=models.CASCADE)
    shutterSpeed = models.ForeignKey(ShutterSpeed, on_delete=models.CASCADE)
    continuousShootingRate = models.IntegerField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    lensMount = models.ForeignKey(LensMount, on_delete=models.CASCADE)
    resolution = models.FloatField()
    cardSlots = models.IntegerField()
    jack = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    weight = models.FloatField()

    def getPrice(self):
        locale.setlocale(locale.LC_ALL, 'vi_VN')
        return locale.currency(self.price, grouping=True).split(',', 1)[0]

    def __str__(self):
        return self.name


class FocalLength(models.Model):
    focalLength = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.focalLength


class Lens(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    focalLength = models.ForeignKey(FocalLength, on_delete=models.CASCADE)
    aperture = models.ForeignKey(Aperture, on_delete=models.CASCADE)
    lensMount = models.ForeignKey(LensMount, on_delete=models.CASCADE)
    lensFormat = models.ForeignKey(LensFormat, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    weight = models.FloatField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    phoneNumber = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    account = models.CharField(max_length=15)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class CameraBill(models.Model):
    Payment_Methods = (
        ('Ship Cod', 'Thanh toán khi nhận hàng'),
        ('Banking', 'Thanh toán qua thẻ tín dụng'),
        ('Amortization', 'Trả góp')
    )
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    paymentMethods = models.CharField(max_length=100, choices=Payment_Methods)
    releaseTime = models.DateTimeField()
    totalMoney = models.FloatField()

    def __str__(self):
        name = self.user.name + str(self.releaseTime)
        return name


class LensBill(models.Model):
    Payment_Methods = (
        ('Ship Cod', 'Thanh toán khi nhận hàng'),
        ('Banking', 'Thanh toán qua thẻ tín dụng'),
        ('Amortization', 'Trả góp')
    )
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentMethods = models.CharField(max_length=100, choices=Payment_Methods)
    releaseTime = models.DateTimeField()
    totalMoney = models.FloatField()

    def __str__(self):
        name = self.user.name + str(self.releaseTime)
        return name
