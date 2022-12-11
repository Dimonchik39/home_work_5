# Создайте два списка — один с названиями языков программирования, 
# другой — с их нумерацией. ['python', 'c#'] [1,2]
# Вам нужно сделать две функции: первая из которых создаст список 
# кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует 
# этот список следующим образом: если сумма очков слова имеет в делителях 
# номер, с которым она в паре в кортеже, то кортеж остается, его номер 
# заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров 
# букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: 
# https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе 
# с преобразованным списком

lang_list = ['C#', 'C++', 'Pascal', 'Python']
number = [i for i in range (1, len(lang_list) + 1)]

def list_tupe(prog, num):
    '''
    Функция создания кортежа/ перевод букв в большие
    '''
    prog = [word.upper() for word in prog]
    res_list = list(zip(num, prog))
    return res_list

result_list = list_tupe(lang_list, number)
print(result_list)

