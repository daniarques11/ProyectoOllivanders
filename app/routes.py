from app import app, bootstrap
from flask import Flask, render_template, jsonify
from GildedRose import GildedRose
from GildedRose import createObjects
import json

listaInventario = createObjects.createItems()
tiendaGildedRose = GildedRose.GildedRose(listaInventario)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/items')
def items():
    inventarioJSON = {}
    inventarioJSON["items"] = tiendaGildedRose.getInventory()
    return json.dumps(inventarioJSON)


@app.route('/update')
def update():
    tiendaGildedRose.updateQuality()
    return index()


@app.route('/backend')
def backend():
    return render_template('Backend/index.html')

@app.route('/insertar')
def insertar():
    return render_template('Backend/insertar.html')

@app.route('/editar')
def editar():
    return render_template('Backend/editar.html')

