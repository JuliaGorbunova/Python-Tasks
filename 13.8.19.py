K = int(input("Введите количество билетов, которые вы желаете приобрести: "))
if K<0:
    print("Количество билетов должно быть положительным числом или нулем")
else:
    B = []
    for i in range(1,K+1):
        v=int(input("Введите возраст посетителя: "))
        if v<=0:
            print("Вы ввели некорректный возраст посетителя. Его билет не будет учтен в общей сумме.")
        else:
            B.append(v)
    S = 0
    for j,value in enumerate(B):
        if value>25:
            S += 1390
        elif 18<=value<=25:
            S+=990  #
    if K>3:
        S*=0.9
    print("Суммарная стоимость билетов будет равна", round(S,2), "рублей")

