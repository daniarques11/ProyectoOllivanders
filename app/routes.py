from app import app, bootstrap
from flask import Flask, render_template, jsonify
from GildedRose import GildedRose
from GildedRose import createObjects


@app.route('/index')
def index():
    listaInventario = createObjects.createItems()
    tiendaGildedRose = GildedRose.GildedRose(listaInventario)
    inventarioJSON = {}
    inventarioJSON["items"] = tiendaGildedRose.getInventory()
    return render_template('index.html', shop=inventarioJSON)


@app.route('/home')
def home():
    return render_template('home.html', home=logica.update(0))


@app.route('/update')
def update():
    return '<h1>Bad Request</h1>', 400


@app.route('/update/<day>')
def update_day(day):
    if not day:
        abort(404)
    return render_template('update.html', day=day, update=logica.update(int(day)))
