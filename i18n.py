#!/usr/bin/env python3
# i18n.py
# Simple language support for the Gourmet Restaurant app

LANG = "es"

_UI = {
    "es": {
        "welcome": "  ¡Bienvenidos a nuestro restaurante!  ",
        "ask_enter": "¿Deseas ingresar a nuestro menú? (s/n): ",
        "bye_visit": "\nGracias por visitarnos. ¡Hasta pronto!",
        "main_title": "             MENÚ PRINCIPAL            ",
        "opt_breakfast": "1. Menú de Desayunos",
        "opt_lunch": "2. Menú de Almuerzos",
        "opt_dessert": "3. Menú de Postres",
        "opt_view_order": "4. Ver Orden y Total",
        "opt_invoice": "5. Confirmar Pedido y Facturar",
        "opt_cancel": "6. Cancelar Orden Actual",
        "opt_admin": "7. Panel de Base de Datos y CRUD (Admin)",
        "opt_lang": "8. Idioma / Language",
        "opt_exit": "0. Salir del Sistema",
        "select_option": "Seleccione una opción (0-8): ",
        "invalid_option": "\nOpción no válida. Por favor elija un número entre 0 y 8.",
        "press_enter": "\nPresione ENTER para continuar...",
        "press_enter_back": "\nPresione ENTER para volver al Menú Principal...",
        "enter_code": "\nIngrese el código del plato que desea agregar (o 0 para volver): ",
        "invalid_code_cat": "Código no válido para esta categoría. Intente nuevamente.",
        "selected": "Ha seleccionado: {name} ({price})",
        "enter_qty": "Ingrese la cantidad que desea: ",
        "qty_gt_zero": "La cantidad debe ser mayor a 0.",
        "qty_int": "Por favor ingrese un número entero válido.",
        "add_more": "¿Desea agregar otro plato de esta sección? (s/n): ",
        "order_empty": "\nNo tiene platos en la orden para facturar.",
        "enter_name": "Ingrese el nombre del cliente: ",
        "default_customer": "Consumidor Final",
        "order_cancelled": "\nOrden cancelada y reiniciada.",
        "goodbye": "\n¡Gracias por preferir Restaurante Gourmet! Que tenga un feliz día.",
        "lang_changed": "\nIdioma cambiado a Español.",
        "header_breakfast": "            DESAYUNOS            ",
        "header_lunch": "            ALMUERZOS            ",
        "header_dessert": "             POSTRES             ",
        "cat_breakfast": "Desayuno",
        "cat_lunch": "Almuerzo",
        "cat_dessert": "Postre",
        "col_code": "Cod",
        "col_dish": "Plato",
        "col_price": "Precio",
        "no_dishes_cat": "  Actualmente no hay platos disponibles en esta categoría.",
        "order_title": "               ORDEN ACTUAL              ",
        "col_qty": "Cant",
        "col_desc": "Descripción",
        "col_unit": "V. Unit",
        "col_subtotal": "Subtotal",
        "order_empty_now": "\n--- La orden está vacía actualmente. ---",
        "subtotal": "SUBTOTAL:",
        "tax": "IMPOCONSUMO (8%):",
        "total": "TOTAL A PAGAR:",
        "invoice_summary": "         RESUMEN DE FACTURA          ",
        "restaurant_name": "                 RESTAURANTE GOURMET                   ",
        "customer": " Cliente: {name}",
        "thanks": "        ¡Gracias por su visita, vuelva pronto!         ",
        "invoice_saved": "\nFactura generada y guardada exitosamente en '{path}'.",
        "invoice_saved_err": "\nNota: Factura generada (no se pudo escribir archivo: {e})",
        "invoice_db_ok": "[PostgreSQL] Pedido registrado en la base de datos con ID #{id}.",
        "invoice_db_fail": "[AVISO] La factura se generó en archivo, pero no pudo registrarse en PostgreSQL.",
        "invoice_local": "[MODO LOCAL] Factura emitida sin persistencia en base de datos (PostgreSQL no conectado).",
        "invoice_db_err": "[AVISO BD] Error al intentar guardar en base de datos: {e}",
        "no_products_invoice": "\nNo hay productos en la orden para facturar.",
        "added_more": "Se agregaron {qty} unidad(es) más de {name}.",
        "added_ok": "¡{name} agregado exitosamente a la orden!",
        "code_not_found": "El código ingresado no existe en la carta.",
        "qty_must_pos": "La cantidad debe ser mayor a cero.",
    },
    "en": {
        "welcome": "     Welcome to our restaurant!      ",
        "ask_enter": "Would you like to view our menu? (y/n): ",
        "bye_visit": "\nThank you for visiting. See you soon!",
        "main_title": "               MAIN MENU              ",
        "opt_breakfast": "1. Breakfast Menu",
        "opt_lunch": "2. Lunch Menu",
        "opt_dessert": "3. Dessert Menu",
        "opt_view_order": "4. View Order and Total",
        "opt_invoice": "5. Confirm Order and Invoice",
        "opt_cancel": "6. Cancel Current Order",
        "opt_admin": "7. Database and CRUD Panel (Admin)",
        "opt_lang": "8. Idioma / Language",
        "opt_exit": "0. Exit System",
        "select_option": "Select an option (0-8): ",
        "invalid_option": "\nInvalid option. Please choose a number between 0 and 8.",
        "press_enter": "\nPress ENTER to continue...",
        "press_enter_back": "\nPress ENTER to return to the Main Menu...",
        "enter_code": "\nEnter the dish code you want to add (or 0 to go back): ",
        "invalid_code_cat": "Invalid code for this category. Please try again.",
        "selected": "You selected: {name} ({price})",
        "enter_qty": "Enter the quantity: ",
        "qty_gt_zero": "Quantity must be greater than 0.",
        "qty_int": "Please enter a valid integer number.",
        "add_more": "Would you like to add another dish from this section? (y/n): ",
        "order_empty": "\nYou have no items in the order to invoice.",
        "enter_name": "Enter customer name: ",
        "default_customer": "Walk-in Customer",
        "order_cancelled": "\nOrder cancelled and reset.",
        "goodbye": "\nThank you for choosing Gourmet Restaurant! Have a great day.",
        "lang_changed": "\nLanguage changed to English.",
        "header_breakfast": "            BREAKFAST            ",
        "header_lunch": "              LUNCH              ",
        "header_dessert": "             DESSERTS            ",
        "cat_breakfast": "Breakfast",
        "cat_lunch": "Lunch",
        "cat_dessert": "Dessert",
        "col_code": "Code",
        "col_dish": "Dish",
        "col_price": "Price",
        "no_dishes_cat": "  There are currently no dishes available in this category.",
        "order_title": "             CURRENT ORDER             ",
        "col_qty": "Qty",
        "col_desc": "Description",
        "col_unit": "Unit",
        "col_subtotal": "Subtotal",
        "order_empty_now": "\n--- The order is currently empty. ---",
        "subtotal": "SUBTOTAL:",
        "tax": "SALES TAX (8%):",
        "total": "TOTAL DUE:",
        "invoice_summary": "            INVOICE SUMMARY           ",
        "restaurant_name": "                 GOURMET RESTAURANT                   ",
        "customer": " Customer: {name}",
        "thanks": "         Thank you for your visit, come again!         ",
        "invoice_saved": "\nInvoice generated and saved successfully at '{path}'.",
        "invoice_saved_err": "\nNote: Invoice generated (could not write file: {e})",
        "invoice_db_ok": "[PostgreSQL] Order saved in database with ID #{id}.",
        "invoice_db_fail": "[WARNING] Invoice was generated, but could not be saved in PostgreSQL.",
        "invoice_local": "[LOCAL MODE] Invoice issued without database persistence (PostgreSQL not connected).",
        "invoice_db_err": "[DB WARNING] Error while trying to save to database: {e}",
        "no_products_invoice": "\nThere are no products in the order to invoice.",
        "added_more": "Added {qty} more unit(s) of {name}.",
        "added_ok": "{name} successfully added to the order!",
        "code_not_found": "The entered code does not exist in the menu.",
        "qty_must_pos": "Quantity must be greater than zero.",
    },
}

_DISH_EN = {
    "1": ("Pistachio Croissant", "Flaky croissant filled with artisanal pistachio cream."),
    "2": ("Crispy Fried Eggs", "Fried eggs with a crispy edge, traditional country style."),
    "3": ("Parisian Toast", "Golden brioche with butter, Gruyère cheese and ham."),
    "4": ("Lemon Croissant", "Croissant filled with soft lemon cream and glaze."),
    "5": ("Walnut Bread", "Artisanal bread baked with selected walnuts."),
    "6": ("Egg Arepa", "Traditional coastal corn arepa filled with fried egg."),
    "7": ("Beef Empanada", "Crispy empanada filled with seasoned shredded beef."),
    "8": ("Chicken Empanada", "Crispy empanada filled with chicken breast and homemade stew."),
    "9": ("Hawaiian Empanada", "Empanada filled with ham, melted cheese and pineapple."),
    "10": ("Chicken Parm", "Breaded chicken breast with homemade marinara sauce and melted mozzarella."),
    "11": ("Tuscan Chicken", "Chicken breast in creamy sauce with sun-dried tomatoes, spinach and garlic."),
    "12": ("Chicken Casserole", "Traditional chicken stew slow-cooked with vegetables and potatoes."),
    "13": ("Mixed Paella", "Spanish rice with assorted seafood, chicken, pork and saffron."),
    "14": ("Pataraska Salmon", "Fresh salmon fillet wrapped in plantain leaf with native spices."),
    "15": ("Tiramisu", "Italian dessert with layers of coffee-soaked sponge, cream cheese and cocoa."),
    "16": ("Dulce de Leche Lava Cake", "Warm cake with molten dulce de leche center, strawberries and vanilla ice cream."),
    "17": ("Chocolate Lava Cake", "Cake with molten dark chocolate center, strawberries and vanilla ice cream."),
    "18": ("Chocolate Stromboli", "Soft cake layers with intense chocolate ganache and coffee."),
    "19": ("Lemon Cheesecake Gelato", "Creamy cheesecake ice cream with lemon notes and cookie crumble."),
    "20": ("Dubai Chocolate Gelato", "Fine chocolate gelato, toasted pistachio cream and crispy pastry."),
    "21": ("Pistachio Gelato", "Artisanal ice cream made with authentic toasted natural pistachio."),
    "22": ("Basque Cheesecake", "Classic San Sebastián-style baked cheesecake, toasted and creamy."),
    "23": ("Baklava", "Turkish pastry with filo dough, chopped nuts and honey syrup."),
    "24": ("Almojábana Cake", "Traditional dessert made with corn and curd with a touch of caramel."),
    "25": ("Neapolitan Ice Cream", "Classic combination of three flavors: strawberry, vanilla and chocolate."),
}

_CAT_DISPLAY = {
    "es": {"Desayuno": "Desayuno", "Almuerzo": "Almuerzo", "Postre": "Postre"},
    "en": {"Desayuno": "Breakfast", "Almuerzo": "Lunch", "Postre": "Dessert"},
}


def tr(key, **kwargs):
    text = _UI.get(LANG, _UI["es"]).get(key, _UI["es"].get(key, key))
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text
    return text


def toggle_lang():
    global LANG
    LANG = "en" if LANG == "es" else "es"
    return LANG


def is_yes(answer):
    a = (answer or "").strip().lower()
    if LANG == "en":
        return a in ("y", "yes", "s", "si", "sí")
    return a in ("s", "si", "sí", "y", "yes")


def dish_name(code, default):
    if LANG == "en" and code in _DISH_EN:
        return _DISH_EN[code][0]
    return default


def dish_desc(code, default):
    if LANG == "en" and code in _DISH_EN:
        return _DISH_EN[code][1]
    return default


def cat_display(cat):
    return _CAT_DISPLAY.get(LANG, _CAT_DISPLAY["es"]).get(cat, cat)
