from datetime import date
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
    description = models.CharField(max_length=1000)
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
    quantityInStock = models.IntegerField(null=True)
    importDate = models.DateField(null=True)
    isDiscount = models.BooleanField(default=False)

    def getQuantityInStockRange(self):
        return range(2, self.quantityInStock + 1)

    def getPriceDiscount(self):
        if self.isDiscount:
            locale.setlocale(locale.LC_ALL, 'vi_VN')
            return locale.currency(self.price - self.price * 0.06, grouping=True).split(',', 1)[0]
        else:
            locale.setlocale(locale.LC_ALL, 'vi_VN')
            return locale.currency(self.price, grouping=True).split(',', 1)[0]

    def getPriceDiscountFloat(self):
        if self.isDiscount:
            return self.price - self.price * 0.06
        else:
            return self.price

    def getPriceFloat(self):
        return self.price

    def getPrice(self):
        locale.setlocale(locale.LC_ALL, 'vi_VN')
        return locale.currency(self.price, grouping=True).split(',', 1)[0]

    def isCamera(self):
        return 1

    def getStatus(self):
        if self.importDate is None:
            return 4, "Sold out"
        if (date.today() - self.importDate).days < 10:
            if 5 > self.quantityInStock > 0:
                return 0, "Hot"
            elif self.quantityInStock == 0:
                return 4, "Sold out"
            elif self.isDiscount:
                return 1, "Discount"
            else:
                return 2, "New"
        elif self.quantityInStock > 0:
            if self.isDiscount:
                return 1, "Discount"
            else:
                return 3, "Stocking"
        else:
            return 4, "Sold out"

    def __str__(self):
        return self.name


class FocalLength(models.Model):
    focalLength = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.focalLength


class Lens(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    price = models.FloatField(validators=[MinValueValidator(100000), MaxValueValidator(100000000)], null=True)
    focalLength = models.ForeignKey(FocalLength, on_delete=models.CASCADE)
    aperture = models.ForeignKey(Aperture, on_delete=models.CASCADE)
    lensMount = models.ForeignKey(LensMount, on_delete=models.CASCADE)
    lensFormat = models.ForeignKey(LensFormat, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    weight = models.FloatField()
    colors = models.ManyToManyField(Color, verbose_name="list of color")
    description = models.CharField(max_length=1000, null=True)
    quantityInStock = models.IntegerField(null=True)
    importDate = models.DateField(null=True)
    isDiscount = models.BooleanField(default=False)

    def getQuantityInStockRange(self):
        return range(2, self.quantityInStock + 1)

    def getPriceDiscount(self):
        if self.isDiscount:
            locale.setlocale(locale.LC_ALL, 'vi_VN')
            return locale.currency(self.price - self.price * 0.06, grouping=True).split(',', 1)[0]
        else:
            locale.setlocale(locale.LC_ALL, 'vi_VN')
            return locale.currency(self.price, grouping=True).split(',', 1)[0]

    def getPriceDiscountFloat(self):
        if self.isDiscount:
            return self.price - self.price * 0.06
        else:
            return self.price

    def getPriceFloat(self):
        return self.price

    def getPrice(self):
        locale.setlocale(locale.LC_ALL, 'vi_VN')
        return locale.currency(self.price, grouping=True).split(',', 1)[0]

    def isCamera(self):
        return 0

    def getStatus(self):
        if self.importDate is None:
            return 4, "Sold out"
        if (date.today() - self.importDate).days < 10:
            if 5 > self.quantityInStock > 0:
                return 0, "Hot"
            elif self.quantityInStock == 0:
                return 4, "Sold out"
            elif self.isDiscount:
                return 1, "Discount"
            else:
                return 2, "New"
        elif self.quantityInStock > 0:
            if self.isDiscount:
                return 1, "Discount"
            else:
                return 3, "Stocking"
        else:
            return 4, "Sold out"

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    phoneNumber = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    account = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, null=True, default="Male")

    def __str__(self):
        return self.name


class CameraBill(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class LenBill(models.Model):
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Bill(models.Model):
    Payment_Methods = (
        ('Cash on delivery', 'Cash on delivery'),
        ('Debit or Credit Card', 'Debit or Credit Card'),
        ('PayPal', 'PayPal')
    )
    cameras = models.ManyToManyField(CameraBill, verbose_name="list of camera bill")
    lens = models.ManyToManyField(LenBill, verbose_name="list of len bill")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentMethods = models.CharField(max_length=100, choices=Payment_Methods)
    address = models.CharField(max_length=1500, null=True)
    instructions = models.CharField(max_length=1500, null=True)
    releaseTime = models.CharField(max_length=200)
    totalMoney = models.FloatField(null=True)
    totalMoneyNoDiscount = models.FloatField(null=True)
    isAccept = models.BooleanField(default=False)
    isCancel = models.BooleanField(default=False)

    def __str__(self):
        name = self.user.name + " " + str(self.releaseTime)
        return name

    def getTotalMoneyNoDiscount(self):
        locale.setlocale(locale.LC_ALL, 'vi_VN')
        return locale.currency(self.totalMoneyNoDiscount, grouping=True).split(',', 1)[0]

    def getTotalMoney(self):
        locale.setlocale(locale.LC_ALL, 'vi_VN')
        return locale.currency(self.totalMoney, grouping=True).split(',', 1)[0]

    def getTotalDiscount(self):
        locale.setlocale(locale.LC_ALL, 'vi_VN')
        return locale.currency(self.totalMoneyNoDiscount - self.totalMoney, grouping=True).split(',', 1)[0]


class Order(models.Model):
    lens = models.ManyToManyField(Lens, verbose_name="list of len")
    cameras = models.ManyToManyField(Camera, verbose_name="list of camera")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        name = self.user.name
        return name
