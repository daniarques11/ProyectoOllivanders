from NormalItem import NormalItem


class GildedRose:

    registerList = []

    def __init__(self,  items):
        self.items = items

    def updateQuality(self):
        for itemClass in self.items:
            itemClass.updateQuality()

    def getInventory(self):
        inventory = []
        for itemClass in self.items:
            inventory.append(itemClass.getSelf())
        return inventory.copy

    def updateRegisterList(self, inventory):
        self.registerList.append(inventory)

    def __repr__(self, passed_days):
        return self.registerList
