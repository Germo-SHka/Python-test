import tkinter as tk

QAl = {1 : "Каким языком является Python?.Aспектно-ориентированный.Логический.Объектно-ориентированный", 2 : "К какому уровню относится язык Python?.К высокому.К низкому.К среднему", 3 : "Основные архитектурные черты Python?.Динамическая типизация, слабая типизация, автоматическое управление памятью.Динамическая типизация, автоматическое управление памятью,полная интроспекция.Aрифметические операции с плавающей точкой относятся к небезопасному коду", 4 : "В каком году был основан язык программирования Python?.1992.1991.1990", 5 : "Какая функция выводит строку в Python?.print().range().input()", 6 : "Присваивание в Python обозначается знаком.«+».«-».«=»", 7 : "Сколькими величинами представлены логические значения в Python?.Двумя.Одной.Тремя", 8 : "Как вычисляется длина строки?.s1 + s2.len(s).s[i:j:k]", 9 : "Что такое кортеж в Python?.Набор разнородных элементов.Обработка данных, выполняемая, в основном, средствами вычислительной техники.Специалист, отвечающий за нормальное функционирование и использование ресурсов", 10 : "Чем задается кортеж?.Вычитаем в квадратных скобках через точку.Умножением в круглых скобках через точку.Перечислением в круглых скобках через запятую"}
f = open("dataQA.txt", "w")
NS = 0
Okresult = [3, 1, 2, 2, 1, 3, 1, 2, 1, 3]
    
def result():
    global f
    f.close
    f = open('dataQA.txt', 'r')
    resultat = f.read().split('\n')
    KPA = 0
    
    for i in range(10):
        if int(resultat[i]) == int(Okresult[i]):
                KPA += 1
                
    Result['text'] = f'Результат:{KPA}/10\n^'
    
def next_Q():
    '''Следующий вопрос'''
    global QAl, NS
    NS += 1
    QA = QAl[NS].split(".")
    Label_1["text"] = f'{str(QA[0])}'
    RB1["text"] = f'{str(QA[1])}'
    RB2["text"] = f'{str(QA[2])}'
    RB3["text"] = f'{str(QA[3])}'
    
def answer():
    '''Сохранение ответа в файл, и вызов следующего вопроса'''
    global ANSWER, f 
    a = str(ANSWER.get()) + "\n"
    f.write(a)
    
    if NS+1 < 11:
        next_Q()
    else:
        Abtn['state'] = 'disable'
        Endbtn['bg'] = 'green'
        Endbtn['state'] = 'normal'
        QTbtn['state'] = 'normal'
        QTbtn['bg'] = 'light green'
    
def End():
    f.close()
    root.iconify()
    
root = tk.Tk()
root.config()
root.attributes('-fullscreen', True)

ANSWER = tk.IntVar(root, value=1)

Label_1 = tk.Label(root, text="None", anchor='w')
Label_1.pack(anchor='w')

RB1 = tk.Radiobutton(root, text="None", variable=ANSWER, value=1, anchor='w')
RB2 = tk.Radiobutton(root, text="None", variable=ANSWER, value=2, anchor='w') 
RB3 = tk.Radiobutton(root, text="None", variable=ANSWER, value=3, anchor='w')

RB1.pack(anchor='w')
RB2.pack(anchor='w')
RB3.pack(anchor='w')

Abtn = tk.Button(root, text="Ответить", command=answer)
Abtn.pack(anchor='w')

QTbtn = tk.Button(root, text='Результат', command=result,  state='disable')
QTbtn.pack(anchor='e')

Endbtn = tk.Button(root, text='Завершить', command=End,  state='disable')
Endbtn.pack(anchor='e')

Result = tk.Label(root, text='Результат:../10\n^')
Result.pack()

next_Q()

root. mainloop()
