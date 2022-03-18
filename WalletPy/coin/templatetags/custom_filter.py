from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter(name='removeBadStr')
def removeBadStr(value):
    textRemove = value.replace('\n',' ')
    textFinal = textRemove.replace('\r',' ')
    return textFinal


@register.filter(name='encode')
def encode(value):
    return value.encode('utf-8').decode()
