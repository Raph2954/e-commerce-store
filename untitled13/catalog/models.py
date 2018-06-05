from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=120, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    description = models.TextField(blank=True)
    Is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='image')
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    Last_updated_at = models.DateTimeField(auto_now=True)


class Meta:
    db_table = 'categories'
    ordering = ['-created_at']
    verbose_name_plural = 'Categories'
def __unicode__(self):
    return self.name
#@models.permalink
def get_absolute_url(self):
    return 'catalog_category', (), {'category_slug': self.slug}


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=150, unique=True,
                        help_text= 'Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2,
                                    blank=True, default=0.00)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(null=False)
    image = models.ImageField(upload_to='image')
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Last_updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
    def __unicode__(self):
        return self.name
    #@models.permalink
    def get_absolute_url(self):
        return 'catalog_product', (), {'product_slug': self.slug}

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


#class CategoryAdmin(admin.ModelAdmin):
    #list_display = 'name','catalog'


#class ProductAdmin(admin.ModelAdmin):
    #list_display = 'name', 'manufacturer', 'description'

class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'Last_updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'Last_updated_at',)
    prepopulated_fields = {'slug': ('name',)}
