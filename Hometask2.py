from typing import Callable, Iterator

# виділяємо дійсні числа з тексту
def generator_numbers(text: str) -> Iterator[float]: 
    # розділяємо текст по пробілам
    for word in text.split(): 
        try:
            yield float(word) # конвертуємо слово в число
        except ValueError:
            continue # якщо це не число - ігноруємо

# рахуємо суму, на основі згенерованих чисел
def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    return sum(func(text))

text = "Загальний дохід: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 999.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(total_income)
