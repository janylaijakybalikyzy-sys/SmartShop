from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review
from django.utils.translation import get_language  # Ушуну коштук

def index(request):
    lang = request.LANGUAGE_CODE  # Учурдагы тилди аныктоо
    
    # Тилдерге жараша котормолор
    translations = {
        'ky': {
            'hero_title': 'Инновация. Сапат. Стиль.',
            'hero_sub': 'Сиз татыктуу болгон эң мыкты технологиялык жыйнак жана премиум гаджеттердин эксклюзивдүү борбору.',
            'welcome': 'Келечектин дүкөнүнө кош келиңиз!',
            'welcome_sub': 'Эң акылдуу гаджеттер жана технологиялар бир гана бизде.',
        },
        'ru': {
            'hero_title': 'Инновация. Качество. Стиль.',
            'hero_sub': 'Эксклюзивный центр лучших технологических коллекций и премиум гаджетов, которых вы достойны.',
            'welcome': 'Добро пожаловать в магазин будущего!',
            'welcome_sub': 'Самые умные гаджеты и технологии только у нас.',
        },
        'en': {
            'hero_title': 'Innovation. Quality. Style.',
            'hero_sub': 'The exclusive center for the best technological collections and premium gadgets you deserve.',
            'welcome': 'Welcome to the store of the future!',
            'welcome_sub': 'The smartest gadgets and technologies only with us.',
        },
        'zh-hans': {
            'hero_title': '创新. 质量. 风格.',
            'hero_sub': '您值得拥有的最佳技术收藏和高端小工具的独家中心。',
            'welcome': '欢迎来到未来的商店！',
            'welcome_sub': '只有我们拥有最智能的小工具和技术。',
        }
    }

    context = {
        'text': translations.get(lang, translations['ky']), # Эгер тил табылбаса, кыргызчасын берет
        # ... калган өзгөрмөлөр (products, categories ж.б.)
    }
    return render(request, 'index.html', context)