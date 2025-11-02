def pruef_rate(rate, antwort):
    global points
    noch_rate = True
    versuch = 0
    while noch_rate and versuch < 3:
        if rate.lower() == antwort.lower():
            print('Right Answer')
            punkte = punkte + 1
            noch_rate = False
        else:
            if versuch < 2:
                rate = input('Wrong, Try again')
            versuch = versuch + 1
    if versuch == 3:
        print('The Answer is right')

    punkte = 0
    print('Find the Animal')
    rate1 = input('Which Bear lives on the North Pole?')
    pruef_antwort(rate1, 'Ice Bear')
    rate2 = input('Which is the fastest land animal?')
    pruef_antwort(rate2, 'Gepard')
    rate3 = input('Which is the biggest Animal?')
    pruef_antwort(rate3, 'Bluewhale')

    print('Your Points: ' + str(punkte))
