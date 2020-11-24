from django.template.defaulttags import register


@register.filter
def get_day_of_week(val):
	if val == 6:
		return "Sunday"
	elif val == 0:
		return "Monday"
	elif val == 1:
		return "Tuesday"
	elif val == 2:
		return "Wednesday"
	elif val == 3:
		return "Thursday"
	elif val == 4:
		return "Friday"		
	elif val == 5:
		return "Saturday"

	

