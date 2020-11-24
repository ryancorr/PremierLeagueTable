from django.template.defaulttags import register


@register.filter
def get_item_two(dictionary, key):
	vals = dictionary.get(key)
	return vals[1]