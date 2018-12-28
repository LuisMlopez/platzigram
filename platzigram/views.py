from django.http import JsonResponse


def order_numbers(request):
	"""Get a list of numbers and return it numbers ordered as a JSon response."""
	numbers = request.GET.get('numbers')

	if isinstance(numbers, str):
		# parse string as list
		numbers = numbers.split(',')
		# parse all list values as int
		numbers = [int(number) for number in numbers]

	if isinstance(numbers, list):
		numbers = sorted(numbers)

	return JsonResponse({'ordered_numbers': numbers})
