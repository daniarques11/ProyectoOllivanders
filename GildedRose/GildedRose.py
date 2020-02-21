from NormalItem import NormalItem
import copy


class GildedRose:

    registerList = []

    def __init__(self,  items):
        self.items = items

    def updateQuality(self):
        for item in self.items:
            item.updateQuality()

    def getInventory(self):
        inventory = []
        for item in self.items:
            itemCopy = copy.deepcopy(item)
            inventory.append(itemCopy.getItemJSon())
        return inventory

    def updateRegisterList(self, inventory):
        self.registerList.append(inventory)

    def __repr__(self):
        shopRepr = ""
        for item in self.items:
            shopRepr = shopRepr + str(item) + "\n"
        return shopRepr
