from GildedRose import GildedRose
from createObjects import createItems


def main(passedDays):
    listaInventario = createItems()
    tiendaGildedRose = GildedRose(listaInventario)

    print('\n' + '---------- DAY 0 ----------')
    tiendaGildedRose.updateRegisterList(tiendaGildedRose.getInventory())
    if passedDays > 0:
        for day in range(0, passedDays):
            print('\n' + '---------- DAY ' + str(day + 1) + ' ----------')
            tiendaGildedRose.updateQuality()
            tiendaGildedRose.updateRegisterList(tiendaGildedRose.getInventory())
    print(tiendaGildedRose.registerList)


if __name__ == "__main__":

    print(main(3))
