from django.db import models
from django.utils import timezone
from accounts.models import OTPRequest
from extensions.utils import  date_convert


class Product(models.Model):
    user = models.ForeignKey(OTPRequest, on_delete=models.CASCADE, related_name='products',blank=True,null=True,verbose_name ='کاربر ')
    location = models.CharField(max_length=150,blank=False,verbose_name ='مکان')
    category = models.CharField(max_length=100,blank=False, verbose_name ="دسته بندی")
    title = models.CharField(max_length=100 ,verbose_name ="عنوان")
    description = models.TextField(verbose_name ="توضیحات")
    publish = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField(default=0, verbose_name ='قیمت')
    address = models.CharField(max_length=150, verbose_name ='آدرس')
    datetime = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
    

    def __str__(self):
        return self.title
    
    def publish_time(self):
        return date_convert(self.publish)
    publish_time.short_description = 'زمان انتشار'



class ProductsImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images',verbose_name ="محصول")
    image = models.ImageField(upload_to='products')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'عکس محصول'
    
    

    def __str__(self):
        
        return "%s" % (self.product.title)

        
