from django.shortcuts import render, get_object_or_404, redirect
from django.utils import translation
from products.models import Product, Category, Review 

def index(request):
    """Башкы бет: Издөө, Фильтр жана 4 тилдүү Инновация/Стиль логикасы"""
    
    # 1. Тилди аныктоо
    cur_lang = translation.get_language()
    
    # 2. Издөө жана категория фильтрлерин алуу
    query = request.GET.get('q') 
    cat_id = request.GET.get('category')
    
    # 3. Базадан маалыматтарды алуу
    categories = Category.objects.all()
    all_products = Product.objects.filter(is_active=True).order_by('-id')

    # Издөө логикасы
    if query:
        all_products = all_products.filter(name__icontains=query)
    
    # Категория логикасы
    if cat_id:
        all_products = all_products.filter(category_id=cat_id)
    
    # 4. Котормолор сөздүгү (Жаңы навигация ачкычтары кошулду)
    translations = {
        'ky': {
            'home': 'Башкы бет', 
            'hero_title': 'Инновация. Сапат. Стиль.',
            'hero_sub': 'Сиз татыктуу болгон эң мыкты технологиялык жыйнак жана премиум гаджеттердин эксклюзивдүү борбору.',
            'welcome': 'Келечектин дүкөнүнө кош келиңиз!',
            'welcome_sub': 'Эң акылдуу гаджеттер жана технологиялар бир гана бизде.',
            'search_label': 'Издөө',
            'search_placeholder': 'Товардын аты...',
            'price_label': 'Баасы (макс)',
            'currency': 'сом',
            'add_btn': 'Кошуу',
            'cart_label': 'Себет',
            'total_label': 'Жалпы',
            'order_btn': 'Заказ берүү',
            'added_text': 'Кошулду',
            'empty_cat': 'Бул категорияда товар жок...',
            'rights': 'Бардык укуктар корголгон.',
            # Жаңы кошулгандар:
            'nav_products': 'Товарлар',
            'nav_contact': 'Байланыш',
            'nav_address': 'Дарек',
        },
        'ru': {
            'home': 'Главная',
            'hero_title': 'Инновация. Качество. Стиль.',
            'hero_sub': 'Эксклюзивный центр лучших технологических коллекций и премиум гаджетов, которых вы достойны.',
            'welcome': 'Добро пожаловать в магазин будущего!',
            'welcome_sub': 'Самые умные гаджеты и технологии только у нас.',
            'search_label': 'Поиск',
            'search_placeholder': 'Название товара...',
            'price_label': 'Цена (макс)',
            'currency': 'сом',
            'add_btn': 'Добавить',
            'cart_label': 'Корзина',
            'total_label': 'Итого',
            'order_btn': 'Оформить заказ',
            'added_text': 'Добавлено',
            'empty_cat': 'В этой категории нет товаров...',
            'rights': 'Все права защищены.',
            # Жаңы кошулгандар:
            'nav_products': 'Товары',
            'nav_contact': 'Контакты',
            'nav_address': 'Адрес',
        },
        'en': {
            'home': 'Home',
            'hero_title': 'Innovation. Quality. Style.',
            'hero_sub': 'The exclusive center for the best technological collections and premium gadgets you deserve.',
            'welcome': 'Welcome to the Store of the Future!',
            'welcome_sub': 'The smartest gadgets and technologies only with us.',
            'search_label': 'Search',
            'search_placeholder': 'Product name...',
            'price_label': 'Price (max)',
            'currency': 'som',
            'add_btn': 'Add',
            'cart_label': 'Cart',
            'total_label': 'Total',
            'order_btn': 'Place Order',
            'added_text': 'Added',
            'empty_cat': 'No products in this category...',
            'rights': 'All rights reserved.',
            # Жаңы кошулгандар:
            'nav_products': 'Products',
            'nav_contact': 'Contact',
            'nav_address': 'Address',
        },
        'zh-hans': {
            'home': '首页',
            'hero_title': '创新. 质量. 风格.',
            'hero_sub': '您值得拥有的最佳技术收藏和高端小工具的独家中心。',
            'welcome': '欢迎来到未来的商店！',
            'welcome_sub': '只有我们拥有最智能的小工具和技术。',
            'search_label': '搜索',
            'search_placeholder': '产品名称...',
            'price_label': '价格 (最高)',
            'currency': '索姆',
            'add_btn': '添加',
            'cart_label': '购物车',
            'total_label': '总额',
            'order_btn': '下订单',
            'added_text': '已添加',
            'empty_cat': '该类别中没有产品...',
            'rights': '版权所有.',
            # Жаңы кошулгандар:
            'nav_products': '产品',
            'nav_contact': '联系方式',
            'nav_address': '地址',
        }
    }

    # Тандалган тилге жараша текстти алуу
    selected_text = translations.get(cur_lang, translations['ky'])

    return render(request, 'index.html', {
        'text': selected_text,
        'products': all_products,
        'categories': categories,
        'selected_category': cat_id,
        'query': query,
        'LANGUAGE_CODE': cur_lang 
    })

def product_detail(request, pk):
    """Товардын деталдуу баракчасы"""
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all().order_by('-created_at')
    
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(pk=pk)[:4]

    if request.method == "POST":
        author = request.POST.get('author')
        text = request.POST.get('text')
        rating = request.POST.get('rating')

        if author and text:
            Review.objects.create(
                product=product,
                author=author,
                text=text,
                rating=rating
            )
            return redirect('product_detail', pk=product.pk)

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews,
        'related_products': related_products,
    })