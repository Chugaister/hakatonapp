from db import models, Session
from bardapi import Bard
import re
from random import shuffle
from time import sleep


def get_word_in_quotes(text):
    match = re.search(r'\*\*(\w+)\*\*', text)
    if match:
        return match.group(1)
    else:
        return None


def classify(job: models.Job):
    sleep(2)
    query = f'{job.title} {job.description}'
    query += """
\nТобі дано опис вакансії. Твоє завдання - визначити якому типу людей з обмеженими можливостями вона підходить. Формуй відповідь максимально критично\
Не пиши висновок, подай інформацію у ненйтральному форматі "з висоти пташиного польоту" Тобі потрібно відповісти лише одним словом:
"leg" - якщо вакансія підходить людині з ампутацією ноги або ніг
"arm" - якщо вакансія підходить людині з ампутацією руки або рук
"armleg" - обидва варіанти зазначені вище
"""
    token = 'dAiwf9V0w7KZApf2hdeMaGu6RHmvFH_JTDLtISf6S-fKbwtiOVU4_LM_KZyCCJwr4XPWkQ.'
    answer = Bard(token=token).get_answer(str(query))['content']
    print(answer)
    result = get_word_in_quotes(answer)
    if result is None:
        print(job.id, "ERROR\n", answer)
    job.disability_category = result
    return result


def main():
    session = Session()
    jobs = session.query(models.Job).filter(models.Job.disability_category.is_(None)).all()
    for job in jobs:
        print(job.id, classify(job))
        session.commit()
    session.close()


if __name__ == '__main__':
    main()
