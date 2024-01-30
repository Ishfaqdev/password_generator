from django.shortcuts import render
import string
import random


def generate_password(request):
    generated_password = None

    if request.method == 'POST':
        total_letters = int(request.POST.get('totalLetters', 8))
        total_symbols = int(request.POST.get('totalSymbols', 2))
        total_numbers = int(request.POST.get('totalNumbers', 2))

        letters = string.ascii_letters
        symbols = '!@#$%^&*()_-+=<>?/[]{}|'
        numbers = string.digits

        all_characters = letters + symbols + numbers
        password_characters = (
            random.sample(letters, total_letters) +
            random.sample(symbols, total_symbols) +
            random.sample(numbers, total_numbers)
        )

        random.shuffle(password_characters)
        generated_password = ''.join(password_characters)

    return render(request, 'password_app/index.html', {'generated_password': generated_password})
