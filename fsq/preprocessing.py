import os

from .models import Faq




def handler(data, path):
    path = path

    if not os.path.exists(path):
        os.makedirs(path)
    for faq in data:
        filename = str(faq.pk) + '.txt'
        with open(os.path.join(path, filename), 'w', encoding="utf-8") as temp_file:
            temp_file.write(faq.question)


