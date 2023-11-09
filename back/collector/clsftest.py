from db import models
from classifier import classify


if __name__ == "__main__":
    test_job = models.Job(
        title="Спеціаліст з обробки документів",
        location="Львів",
        description=""""
ПриватБанк — є найбільшим банком України та одним з найбільш інноваційних банків світу. Займає лідуючі позиції за всіма фінансовими показниками в галузі та складає близько чверті всієї банківської системи країни.

Ми шукаємо Спеціаліста з обробки документів, який прагне працювати в динамічному середовищі та розділяє цінності взаємної довіри, відкритості та ініціативності.

Ми прагнемо знайти цілеспрямованого професіонала, який вміє працювати в режимі багатозадачності, орієнтованого на якість та результат.

Основні вимоги:

Вища освіта (інститути, академії, університети), неповна вища освіта
Досвід роботи із документами не менше року
Досвід роботи на ПК
Досвід роботи у великому колективі
Вміння брати на себе відповідальність
Вміння запам’ятовувати інформацію
Навички роботи з оргтехнікою та ПК
Впевнений користувач пакету MS Office
Знання української мови
Робота з ПК на рівні досвідченого користувача (обов'язкові знання WORD,EXСEL та/або OPEN OFFICE)
Вміння знаходити спільну мову із колегами
Основні обов’язки:

Приймання від структурних підрозділів банку на зберігання документів на паперових носіях та забезпечення розміщення та обліку коробів з документами
Здійснення вибіркового розкриття конвертів та перевірки коректності документів
Виконання в нормативні терміни запитів Управління з розшуку документів на надання оригіналів (пошук документів, підготовка документів до відправлення, та закриття запиту відповідно до вимог)
Дотримання порядку і правил використання та зберігання документів
Участь в проведенні експертизи цінності документів
Перевірка коробів під час вивезення документів для знищення, підготовка та вилучення документів, термін зберігання яких закінчився
Відправка документів, виклик кур'єра, підготовка супровідних документів і та ін.
Своїм співробітникам ми пропонуємо:

Роботу в найбільшому та інноваційному банку України
Офіційне працевлаштування та 24 календарних дні відпустки
Конкурентну заробітну плату
Медичне страхування та корпоративний мобільний зв’язок
Корпоративне навчання
Сучасний комфортний офіс
Цікаві проєкти, амбіційні задачі та динамічний розвиток
Дружній професійний колектив та сильну команду
Ви не впевнені, чи надсилати резюме? Думаєте, що на заваді буде зрілий вік або обмеження через стан здоров’я та фізичні можливості?

Не сумнівайтеся. ПриватБанк надає рівні можливості всім кандидатам і вітає у своїй команді різноманітність.

Ми переконані, що різноманітність та інклюзія допомагають досягати амбітних результатів у бізнесі й щодня створювати омріяне майбутнє для громадян. Усі кваліфіковані кандидати отримують рівні можливості під час відбору на вакантні посади незалежно від расової чи етнічної належності, статі, віку, сімейного стану та інвалідності.

Якщо ви маєте статус особи з інвалідністю, ми надамо вам додаткову допомогу й супровід упродовж процесу відбору.

Просимо звертатися на [відгукнутися] для особистої консультації щодо вакансії, яка вас зацікавила. Банк докладає максимум зусиль для створення робочих місць відповідно до вимог певного статусу.    
""",
        salary="19720 грн",
        disable_category=None
    )
    classify(test_job)
    print(test_job.disable_category)
