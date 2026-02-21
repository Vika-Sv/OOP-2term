
sample_text = input('Enter the word or sentences:')
count_lower_delegate = lambda text: sum(1 for ch in text if ch.islower())
print('Count of symbols:', count_lower_delegate(sample_text))
