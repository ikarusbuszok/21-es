
def pontszamitas(lapok: [int]):
    pontok:int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
        return pontok








def eredmenyek(jatekoslapok:[int], geplapok:[int]):
    if jatekoslapok >= 21:
        print("Játékos vesztett")
    elif geplapok >= 21:
        print("Gép vesztett")










