from django.db import models

# 1. КАТЕГОРИЯ
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категориянын аты")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категориялар"

# 2. ТОВАР
class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='products', 
        verbose_name="Категория"
    )
    name = models.CharField(max_length=200, verbose_name="Товардын аты")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баасы")
    image = models.ImageField(upload_to='products/', verbose_name="Негизги сүрөтү")
    description = models.TextField(blank=True, verbose_name="Толук сүрөттөмөсү")
    
    # Техникалык мүнөздөмөлөр үчүн (Мисалы: RAM: 16GB)
    specification = models.JSONField(default=dict, blank=True, verbose_name="Мүнөздөмөлөрү (JSON)")
    
    is_active = models.BooleanField(default=True, verbose_name="Сатыкта бар")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Кошулган күнү")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товарлар"

# 3. ТОВАРДЫН ГАЛЕРЕЯСЫ (Бир товарга бир нече сүрөт)
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, 
        related_name='images', 
        on_delete=models.CASCADE, 
        verbose_name="Товар"
    )
    image = models.ImageField(upload_to='products/gallery/', verbose_name="Кошумча сүрөт")

    class Meta:
        verbose_name = "Товардын сүрөтү"
        verbose_name_plural = "Товардын галереясы"

# 4. ПИКИРЛЕР (Reviews & Ratings)
class Review(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='reviews', 
        verbose_name="Товар"
    )
    author = models.CharField(max_length=100, verbose_name="Аты-жөнү")
    text = models.TextField(verbose_name="Пикир")
    rating = models.IntegerField(default=5, verbose_name="Баа (1-5)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Калтырылган күнү")

    class Meta:
        verbose_name = "Пикир"
        verbose_name_plural = "Пикирлер"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.product.name}"