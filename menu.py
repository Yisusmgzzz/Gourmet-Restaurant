#!/usr/bin/env python3
# menu.py
# NOMBRES DE LOS INTEGRANTES DEL PROYECTO:
# JESUS ESTEBAN MUNOZ GOMEZ
# ALBEIRO ANDRES RODGERS PEREZ
# ALEX JAVIER CAMPO SUAREZ

import titles as t
import i18n

# Base de datos de platos por categoria
# Estructura: codigo, nombre, precio, descripcion, categoria
PLATOS = {
    # --- DESAYUNOS ---
    "1": {
        "nombre": "Croissant Pistacho",
        "precio": 12000,
        "descripcion": "Croissant hojaldrado relleno de crema de pistacho artesanal.",
        "categoria": "Desayuno"
    },
    "2": {
        "nombre": "Huevos Puntilla",
        "precio": 9500,
        "descripcion": "Huevos fritos con borde crujiente al estilo tradicional campesino.",
        "categoria": "Desayuno"
    },
    "3": {
        "nombre": "Tostada Parisina",
        "precio": 11000,
        "descripcion": "Pan brioche dorado con mantequilla, queso gruyère y jamón.",
        "categoria": "Desayuno"
    },
    "4": {
        "nombre": "Croissant Lemon",
        "precio": 10500,
        "descripcion": "Croissant relleno de suave crema de limón y glaseado.",
        "categoria": "Desayuno"
    },
    "5": {
        "nombre": "Pan de Nuez",
        "precio": 6500,
        "descripcion": "Pan artesanal horneado con nueces seleccionadas.",
        "categoria": "Desayuno"
    },
    "6": {
        "nombre": "Arepa de Huevo",
        "precio": 6000,
        "descripcion": "Típica arepa costeña de maíz amarillo rellena con huevo frito.",
        "categoria": "Desayuno"
    },
    "7": {
        "nombre": "Empanada de Carne",
        "precio": 4500,
        "descripcion": "Empanada crujiente rellena de carne desmechada sazonada.",
        "categoria": "Desayuno"
    },
    "8": {
        "nombre": "Empanada de Pollo",
        "precio": 4500,
        "descripcion": "Empanada crocante rellena de pechuga de pollo y guiso casero.",
        "categoria": "Desayuno"
    },
    "9": {
        "nombre": "Empanada Hawaiana",
        "precio": 4500,
        "descripcion": "Empanada rellena de jamón, queso derretido y piña calada.",
        "categoria": "Desayuno"
    },

    # --- ALMUERZOS ---
    "10": {
        "nombre": "Chicken Parm",
        "precio": 28000,
        "descripcion": "Pechuga empanizada con salsa marinara casera y queso mozzarella gratinado.",
        "categoria": "Almuerzo"
    },
    "11": {
        "nombre": "Pollo Toscano",
        "precio": 29500,
        "descripcion": "Pechuga en salsa cremosa de tomates secos, espinacas y ajo.",
        "categoria": "Almuerzo"
    },
    "12": {
        "nombre": "Pollo a la Cacerola",
        "precio": 26000,
        "descripcion": "Guiso tradicional de pollo cocinado a fuego lento con vegetales y papas.",
        "categoria": "Almuerzo"
    },
    "13": {
        "nombre": "Paella Mixta",
        "precio": 35000,
        "descripcion": "Arroz español con mariscos variados, pollo, cerdo y azafrán.",
        "categoria": "Almuerzo"
    },
    "14": {
        "nombre": "Salmón Pataraska",
        "precio": 38000,
        "descripcion": "Filete de salmón fresco envuelto en hoja de plátano con especias autóctonas.",
        "categoria": "Almuerzo"
    },

    # --- POSTRES ---
    "15": {
        "nombre": "Tiramisú",
        "precio": 16900,
        "descripcion": "Postre italiano con capas de bizcocho al café, crema de queso y cacao.",
        "categoria": "Postre"
    },
    "16": {
        "nombre": "Volcán de Arequipe",
        "precio": 17900,
        "descripcion": "Bizcocho tibio con centro fundido de arequipe, fresas y helado de vainilla.",
        "categoria": "Postre"
    },
    "17": {
        "nombre": "Volcán de Chocolate",
        "precio": 17900,
        "descripcion": "Bizcocho con centro líquido de chocolate oscuro, fresas y helado de vainilla.",
        "categoria": "Postre"
    },
    "18": {
        "nombre": "Stromboli de Chocolate",
        "precio": 17900,
        "descripcion": "Capas de bizcocho suave con ganache de chocolate intenso y café.",
        "categoria": "Postre"
    },
    "19": {
        "nombre": "Gelato Cheese de Limón",
        "precio": 7500,
        "descripcion": "Helado cremoso de tarta de queso con notas de limón y crumble de galleta.",
        "categoria": "Postre"
    },
    "20": {
        "nombre": "Gelato Chocolate Dubai",
        "precio": 17900,
        "descripcion": "Gelato de chocolate fino, crema de pistacho tostado y crujiente de hojaldre.",
        "categoria": "Postre"
    },
    "21": {
        "nombre": "Gelato Pistaccio",
        "precio": 7500,
        "descripcion": "Helado artesanal elaborado con auténtico pistacho natural tostado.",
        "categoria": "Postre"
    },
    "22": {
        "nombre": "Tarta Vasca",
        "precio": 15000,
        "descripcion": "Clásica cheesecake horneada al estilo San Sebastián, tostada y cremosa.",
        "categoria": "Postre"
    },
    "23": {
        "nombre": "Baklava",
        "precio": 13500,
        "descripcion": "Dulce turco de masa filo relleno de nueces picadas y bañado en miel.",
        "categoria": "Postre"
    },
    "24": {
        "nombre": "Torta de Almojábana",
        "precio": 11000,
        "descripcion": "Postre tradicional a base de maíz y cuajada con toque de caramelo.",
        "categoria": "Postre"
    },
    "25": {
        "nombre": "Helado Napolitano",
        "precio": 6500,
        "descripcion": "Combinación clásica de tres sabores: fresa, vainilla y chocolate.",
        "categoria": "Postre"
    }
}


def mostrar_categoria(categoria_filtro):
    """Muestra los platos correspondientes a una categoria dada."""
    if categoria_filtro == "Desayuno":
        t.breakfast_menu()
    elif categoria_filtro == "Almuerzo":
        t.midfood_menu()
    elif categoria_filtro == "Postre":
        t.desserts_menu()

    print(f"{i18n.tr('col_code'):<5}{i18n.tr('col_dish'):<30}{i18n.tr('col_price'):>10}")
    print("-" * 47)
    
    encontrados = []
    for cod, datos in PLATOS.items():
        if datos["categoria"] == categoria_filtro:
            encontrados.append(cod)
            precio_fmt = f"${datos['precio']:,}".replace(",", ".")
            nombre = i18n.dish_name(cod, datos['nombre'])
            desc = i18n.dish_desc(cod, datos['descripcion'])
            print(f"[{cod:>2}] {nombre:<28} {precio_fmt:>12}")
            print(f"      -> {desc}")
            print()

    if not encontrados:
        print(i18n.tr("no_dishes_cat"))
        print()

    print("-" * 47)
    return encontrados
