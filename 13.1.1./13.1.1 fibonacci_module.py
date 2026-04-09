def generate_fibonacci_sequence(max_value):
	if max_value <= 0:
		return []

	sequence = []
	a = 0
	b = 1

	while a <= max_value:
		sequence.append(a)
		a, b = b, a + b
	return sequence
