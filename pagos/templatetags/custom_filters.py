from django import template

register = template.Library()

@register.filter(name='sum_total')
def sum_total(data, key):
    """
    Suma los valores de una clave específica en un diccionario.
    'data' se asume que es un diccionario cuyos valores son también diccionarios.
    Por ejemplo: data = {
        'item1': {'precio': 100, 'cantidad': 2},
        'item2': {'precio': 200, 'cantidad': 1}
    }
    key = 'precio'
    sum_total(data, 'precio') devolvería 300.
    """
    return sum(item.get(key, 0) for item in data.values()) if hasattr(data, 'values') else 0


@register.filter(name='sum')
def sum_field(data, field_name):
    """
    Suma los valores de un campo específico en una lista de diccionarios.
    Por ejemplo: data = [{'precio': 100}, {'precio': 200}]
    sum_field(data, 'precio') devolvería 300.
    """
    return sum(item.get(field_name, 0) for item in data) if isinstance(data, list) else 0


@register.filter(name='floatformat')
def custom_floatformat(value, precision):
    """
    Formatea un número como float con la precisión especificada.
    Por ejemplo: custom_floatformat(123.4567, 2) -> '123.46'
    """
    try:
        return f'{float(value):.{precision}f}'
    except (ValueError, TypeError):
        return value


@register.filter(name='format_currency')
def format_currency(value):
    """
    Formatea un valor numérico como moneda.
    Convierte enteros en un formato con puntos, por ejemplo:
    format_currency(10000) -> '$10.000'
    """
    try:
        return f"${int(value):,}".replace(",", ".")
    except (ValueError, TypeError):
        return value


@register.filter
def add_class(field, css_class):
    """
    Agrega una clase CSS a un campo de formulario.
    Por ejemplo, en la plantilla:
    {{ form.campo|add_class:"form-control" }}
    """
    return field.as_widget(attrs={"class": css_class})


@register.filter
def get_item(dictionary, key):
    """
    Devuelve el valor asociado a 'key' en el diccionario.
    Si no existe, devuelve 0.
    Por ejemplo: get_item({'a': 1, 'b': 2}, 'a') -> 1
    """
    if isinstance(dictionary, dict):
        return dictionary.get(key, 0)
    return 0


@register.filter
def split(value, arg):
    """
    Divide una cadena con un separador dado.
    Por ejemplo: "Enero,Febrero,Marzo"|split:"," -> ["Enero", "Febrero", "Marzo"]
    """
    if isinstance(value, str):
        return value.split(arg)
    return value
