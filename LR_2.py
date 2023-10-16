print("\tКалькулятор депозиту")
introduction = input("Якщо хочете дізнатися, як працює калькулятор депозиту, то напишіть (так/ні): ")
if introduction == "так":
    print("Калькулятор депозиту допоможе Вам розрахувати, скільки грошей Ви заробите на своєму депозиті.\n Вам потрібно ввести:\n\t1) Суму депозиту.\n\t2) Річну ставку, котру надає банк.\n\t3) Термін дії депозиту.")
    print("Наприклад, Ви вносите 1000 грн на 12 місяців під 12% річних, тобто кожного місяця до 1000 грн буде додаватися 12%/12міс = 1%.\n Тобто через місяць у Вас на рахунку буде 1010 грн.\n А ще через місяць річний відсоток береться від суми 1010 грн. Тобто будемо мати 1020.1 грн.")
   
else:
    print("Давайте рахувати гроші!")

def calculate_deposit():
    while True:
        try:
            deposit_amount = float(input("Введіть суму депозиту: "))
            annual_interest_rate = float(input("Введіть річні відсотки: "))
            months = int(input("Введіть тривалість депозиту у місяцях: "))
            
            if deposit_amount <= 0 or annual_interest_rate < 0 or months <= 0:
                print("Невірні дані. Сума депозиту та тривалість мають бути більше нуля, а річні відсотки - не менше нуля.")
                continue

            monthly_interest_rate = annual_interest_rate / 12 / 100
            total_amount = deposit_amount

            for month in range(1, months + 1):
                interest_earned = total_amount * monthly_interest_rate
                total_amount += interest_earned
                print(f"Місяць {month}: Загальна сума вкладу: {total_amount:.2f}, Нараховані відсотки: {interest_earned:.2f}")

            print(f"Після {months} місяців ви отримаєте {total_amount:.2f} на вашому депозиті.")
            break

        except ValueError:
            print("Невірний формат введених даних. Будь ласка, введіть числа.")

calculate_deposit()

    


