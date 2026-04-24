import requests

def ask_ai(prompt):
    print("Делаю запрос AI")
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    print("Ответ получен")
    data = response.json()
    return data["response"].strip()

# дополнить словарь
WORDS = {
    "hello": "привет",
    "cat": "кот",
    "dog": "собака",
    "apple": "яблоко",
    "car": "машина",
    'terminal': 'aэровокзал',
    'entrance': 'вход',
    'exit': 'выход',
    'arrivals': 'прибытие',
    'departures': 'отправление',
    'flight': 'рейс самолёта',
    'landing': 'посадка самолёта',
    'information': 'справочное бюро',
    'time of departure': 'время отправления',
    'check-in': 'регистрация',
    'passport control': 'паспортный контроль',
    'gate': 'выход на посадку',
    'customs': 'таможня',
    'luggage claim': 'выдача багажа',
    'lost and Found': 'бюро забытых вещей',
    'delay': 'опоздание, рейс откладывается',
    'duty-free shop': 'магазин беспошлинной торговли',
    'security': 'служба безопасности',
    'toilet, WC': 'туалет',
    'first name': 'имя',
    'family name': 'фамилия',
    'surname': 'фамилия',
    'male': 'пол мужской',
    'female': 'женский',
    'date of birth': 'дата рождения',
    'place of birth': 'место рождения',
    'citizenship': 'гражданство',
    'nationality': 'национальность',

}
REVERSE_WORDS = {v: k for k, v in WORDS.items()}

# перевод 
def translate_word(word):
    word = word.lower().strip()
    if word in WORDS:
        return WORDS[word]
    elif word in REVERSE_WORDS:
        return REVERSE_WORDS[word]
    return None
def request_translation(word):
    result = ask_ai(f"Переведи '{word}'. Ответ: перевод: <слово>")
    return result
def translate_mode():
    word = input("Введите слово: ")
    translated = translate_word(word)
    if translated:
        print(f'{word} → {translated}')
    else:
        result = request_translation(word)
        print(result)

# лексика
def get_topic():
    return input("Введите тему: ")

def request_words(topic):
    return ask_ai(f"Дай 5 английских слов по теме '{topic}' с переводом")

def print_words(words):
    print("\nСлова:")
    print(words)

def extract_pair(line):
    en = line.split("-")[0].strip()
    ru = line.split("-")[1].strip()
    return en, ru

def ask_user(en):
    return input(f"Переведи '{en}': ")

def check_answer(answer, ru):
    return ru.lower() in answer.lower()

def print_result(is_correct, ru):
    if is_correct:
        print("правильно")
    else:
        print(f"правильно: {ru}")

def run_check(words):
    print("\nПроверка:")

    for line in words.split("\n"):
        if "-" in line:
            en, ru = extract_pair(line)
            answer = ask_user(en)
            result = check_answer(answer, ru)
            print_result(result, ru)

def vocabulary_mode():
    topic = get_topic()
    words = request_words(topic)
    print_words(words)
    run_check(words)

# грамматика
def grammar_mode():
    topic = input("Тема: ")

    task = ask_ai(f"Сделай 3 задания по теме {topic} с вопросами")

    print("\nЗадания:")
    print(task)

    user_answers = input("\nНапиши ответы: ")

    check = ask_ai(
        f"Проверь ответы ученика.\nЗадание:\n{task}\nОтветы:\n{user_answers}\nКоротко скажи правильно или нет"
    )

    print("\nРезультат:")
    print(check)

#  беседа

def chat_mode():
    print("Начните диалог (напишите exit для выхода)\n")

    while True:
        sentence = input("Ты: ")

        if sentence.lower() == "exit":
            break

        response = ask_ai(
            f"Ты учитель английского. Отвечай просто и дружелюбно. Исправляй ошибки.\nПользователь: {sentence}"
        )

        print("AI:", response)

vocabulary_choice = "1" 
grammar_choice = "2"
chat_choice = "3"
translate_choice = "4"
exit_choice = "0"

# меню
def main():
    choice = "*"
    while choice != exit_choice:
        print("\nВыберите режим:")
        print(f"{vocabulary_choice}. Лексика")
        print(f"{grammar_choice}. Грамматика")
        print(f"{chat_choice}. Беседа")
        print(f"{translate_choice}. Перевод")
        print(f"{exit_choice}. Выход")

        choice = input("Ваш выбор: ")

        if choice == vocabulary_choice:
            vocabulary_mode()
        elif choice == grammar_choice:
            grammar_mode()
        elif choice == chat_choice:
            chat_mode()
        elif choice == translate_choice:
            translate_mode()
        elif choice == exit_choice:
            break
        else:
            print("Выберите из предложенного")

if __name__ == "__main__":
    main()