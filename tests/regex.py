import re

texts = [
    '/index.php?format=feed&type=rss',
    '/index.php?format=feed&type=atom',
    'https://www2.santoandre.sp.gov.br/images/favicon.png',
    'https://www2.santoandre.sp.gov.br/index.php/component/search/?Itemid=101&format=opensearch',
    '/index.php?option=com_ajax&plugin=arkbootstrap&format=json',
    '/index.php?option=com_ajax&plugin=arktypography&format=json',
    '/media/k2/assets/css/k2.fonts.css?v2.7.1',
    '/templates/gk_news/css/k2.css?v2.7.1',
    '/plugins/content/simplepopup/simplepopup/spustyle.css',
    '/plugins/content/simplepopup/simplepopup/fancybox/jquery.fancybox-1.3.4.css',
    '/plugins/system/jcemediabox/css/jcemediabox.css?3ab6d4490e67378d035cce4c84ffa080',
    '/plugins/system/jcemediabox/themes/standard/css/style.css?7361405241320e69bc1bfb093eb0a2f7',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/k2.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/normalize.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/global.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/joomla.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/system/app.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/template.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/menu/menu.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/gk.stuff.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/style2.css',
    'https://www2.santoandre.sp.gov.br/media/editors/arkeditor/css/squeezebox.css',
    'https://www2.santoandre.sp.gov.br/modules/mod_image_show_gk4/styles/gk_fashion/style.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/small.desktop.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/tablet.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/small.tablet.css',
    'https://www2.santoandre.sp.gov.br/templates/gk_news/css/mobile.css'
]

for text in texts:
    test = re.search('(app|main|styles?|global|estilos?|default).css', text)
    print(test, test is not None, text)
