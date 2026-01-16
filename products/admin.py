from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, Category, ProductImage, Review

# 1. Категорияны каттоо
admin.site.register(Category)

# 2. Галерея үчүн (Товардын ичинде бир нече сүрөт кошуу мүмкүнчүлүгү)
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Жаңы товар кошкондо автоматтык түрдө 3 бош орун көрсөтөт
    verbose_name = "Кошумча сүрөт"
    verbose_name_plural = "Галерея"

# 3. Товарды каттоо
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Тизмеде көрүнө турган талаалар
    list_display = ('get_html_photo', 'name', 'category', 'price', 'is_active')
    
    # Басканда ичине кирүүчү талаалар
    list_display_links = ('get_html_photo', 'name')
    
    # Оң жактагы фильтр
    list_filter = ('category', 'is_active', 'price')
    
    # Издөө талаасы
    search_fields = ('name', 'description')
    
    # Тизмеден эле өзгөртүү
    list_editable = ('price', 'is_active')

    # Галереяны товардын ичине интеграциялоо
    inlines = [ProductImageInline]

    # Сүрөттү админкада көрсөтүү функциясы
    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50 style='border-radius:5px;'>")
        return "Сүрөт жок"

    get_html_photo.short_description = "Сүрөт"

# 4. Пикирлерди каттоо
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('author', 'text')
    # Пикирлерди оңдоого мүмкүн болбосун десеңиз, readonly_fields колдонсо болот