

count_lower_delegate = lambda text: sum(1 for ch in text if ch.islower())

count_lower_lambda = lambda text: len([ch for ch in text if ch.islower()])

sample_text = "Hello World! Python Is FUN"

print("Кількість малих літер (анонімний метод):", count_lower_delegate(sample_text))
print("Кількість малих літер (лямбда-вираз):", count_lower_lambda(sample_text))
