function loadItems() {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var itemsDict = JSON.parse(this.responseText);

            var taula = document.getElementById("itemsTable");

            taula.innerHTML = "";

            for (let item in itemsDict.items) {
                var newRow = taula.insertRow(-1);

                var numColumn = newRow.insertCell(0);
                var imageColumn = newRow.insertCell(1);
                var nameColumn = newRow.insertCell(2);
                var sellInColumn = newRow.insertCell(3);
                var qualityColumn = newRow.insertCell(4);


                numColumn.innerHTML = parseInt(item) + 1;
                var itemName = itemsDict.items[item].name;
                var fileName = "img/" + itemName + ".jpg";
                imageColumn.innerHTML = "<img src='static/" + fileName + "'  alt='...' class='img-fluid' style='width: 80px;'/>";
                nameColumn.innerHTML = itemsDict.items[item].name;
                sellInColumn.innerHTML = itemsDict.items[item].sellIn;
                qualityColumn.innerHTML = itemsDict.items[item].quality;
            }
            //document.getElementById("demo").innerHTML = itemsDict.name;
        }
    };
    xmlhttp.open("GET", "/items", true);
    xmlhttp.send();
}

window.onload = function () {
    loadItems();
};