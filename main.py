
def pontszamitas(lapok: [int]):
    pontok:int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
        return pontok








def eredmenyek(jatekoslapok:[int], geplapok:[int]):
    szöveg=""
    jatekoslapok: int=pontszamitas(lapok)
    geplapok: int=pontszamitas(lapok)
    if jatekoslapok > 21:
        print("Játékos vesztett")
    elif geplapok > 21:
        print("Gép vesztett")



def JatekosVesztettTeszt():
    jatekosLista = [10, 3, 3,]
    gepLista = [6, 10]
    kapott = eredmeny(jatekosLista, gepLista)
    vart = "Játékos vesztett"
    if kapott == vart:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")

def tesztek():
    JatekosVesztettTeszt()

Tesztek()

















