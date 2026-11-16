#!/usr/bin/env python3
# restaurant.py
# Logica de gestion del restaurante y pedidos

import os
from menu import PLATOS
import i18n

# Estructura del pedido actual: lista de diccionarios
# cada elemento: {"codigo": str, "nombre": str, "precio": float, "cantidad": int, "subtotal": float}
orden_actual = []


def agregar_producto(codigo, cantidad):
    """Agrega un producto y su cantidad a la orden."""
    if codigo not in PLATOS:
        return False, i18n.tr("code_not_found")

    if cantidad <= 0:
        return False, i18n.tr("qty_must_pos")

    plato = PLATOS[codigo]
    subtotal = plato["precio"] * cantidad
    nombre = i18n.dish_name(codigo, plato["nombre"])

    # Si ya esta en la orden, sumamos la cantidad
    for item in orden_actual:
        if item["codigo"] == codigo:
            item["cantidad"] += cantidad
            item["subtotal"] += subtotal
            return True, i18n.tr("added_more", qty=cantidad, name=nombre)

    # Si es nuevo en la orden
    orden_actual.append({
        "codigo": codigo,
        "nombre": plato["nombre"],
        "precio": plato["precio"],
        "cantidad": cantidad,
        "subtotal": subtotal
    })
    return True, i18n.tr("added_ok", name=nombre)


def ver_orden():
    """Muestra el estado actual del carrito de compras."""
    if not orden_actual:
        print(i18n.tr("order_empty_now"))
        return 0, 0, 0

    print("\n" + "=" * 55)
    print(i18n.tr("order_title"))
    print("=" * 55)
    print(f"{i18n.tr('col_qty'):<6}{i18n.tr('col_desc'):<26}{i18n.tr('col_unit'):>10}{i18n.tr('col_subtotal'):>12}")
    print("-" * 55)

    subtotal_general = 0
    for item in orden_actual:
        precio_u_fmt = f"${item['precio']:,}".replace(",", ".")
        subtot_fmt = f"${item['subtotal']:,}".replace(",", ".")
        nombre = i18n.dish_name(item["codigo"], item["nombre"])
        print(f"{item['cantidad']:<6}{nombre:<26}{precio_u_fmt:>10}{subtot_fmt:>12}")
        subtotal_general += item["subtotal"]

    iva = subtotal_general * 0.08  # 8% impuesto al consumo para restaurantes
    total = subtotal_general + iva

    print("-" * 55)
    print(f"{i18n.tr('subtotal'):<42} {f'${int(subtotal_general):,}'.replace(',', '.'):>12}")
    print(f"{i18n.tr('tax'):<42} {f'${int(iva):,}'.replace(',', '.'):>12}")
    print(f"{i18n.tr('total'):<42} {f'${int(total):,}'.replace(',', '.'):>12}")
    print("=" * 55)

    return subtotal_general, iva, total


def cancelar_orden():
    """Limpia la orden actual."""
    orden_actual.clear()
    print(i18n.tr("order_cancelled"))


def generar_factura(nombre_cliente=None):
    """Genera la factura final en pantalla y guarda copia en archivo de texto."""
    if nombre_cliente is None:
        nombre_cliente = i18n.tr("default_customer")
    if not orden_actual:
        print(i18n.tr("no_products_invoice"))
        return False

    subtotal, iva, total = ver_orden()

    factura_txt = []
    factura_txt.append("=======================================================")
    factura_txt.append(i18n.tr("restaurant_name"))
    factura_txt.append("                  NIT: 900.123.456-7                   ")
    factura_txt.append(i18n.tr("customer", name=nombre_cliente))
    factura_txt.append("-------------------------------------------------------")
    factura_txt.append(f"{i18n.tr('col_qty'):<6}{i18n.tr('col_desc'):<26}{i18n.tr('col_unit'):>10}{i18n.tr('col_subtotal'):>12}")
    factura_txt.append("-------------------------------------------------------")

    for item in orden_actual:
        precio_u_fmt = f"${item['precio']:,}".replace(",", ".")
        subtot_fmt = f"${item['subtotal']:,}".replace(",", ".")
        nombre = i18n.dish_name(item["codigo"], item["nombre"])
        factura_txt.append(f"{item['cantidad']:<6}{nombre:<26}{precio_u_fmt:>10}{subtot_fmt:>12}")

    factura_txt.append("-------------------------------------------------------")
    factura_txt.append(f"{i18n.tr('subtotal'):<42} {f'${int(subtotal):,}'.replace(',', '.'):>12}")
    factura_txt.append(f"{i18n.tr('tax'):<42} {f'${int(iva):,}'.replace(',', '.'):>12}")
    factura_txt.append(f"{i18n.tr('total'):<42} {f'${int(total):,}'.replace(',', '.'):>12}")
    factura_txt.append("=======================================================")
    factura_txt.append(i18n.tr("thanks"))

    contenido = "\n".join(factura_txt)

    # Guardar en archivo para respaldo universitario
    try:
        ruta_factura = os.path.join(os.path.dirname(__file__), "factura_venta.txt")
        with open(ruta_factura, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(i18n.tr("invoice_saved", path=ruta_factura))
    except Exception as e:
        print(i18n.tr("invoice_saved_err", e=e))

    # Persistencia en PostgreSQL si el modulo esta disponible
    try:
        import crud_restaurante as cr
        if cr.esta_conectado():
            id_ped = cr.guardar_pedido_bd(nombre_cliente, orden_actual, subtotal, iva, total)
            if id_ped:
                print(i18n.tr("invoice_db_ok", id=id_ped))
            else:
                print(i18n.tr("invoice_db_fail"))
        else:
            print(i18n.tr("invoice_local"))
    except Exception as e:
        print(i18n.tr("invoice_db_err", e=e))

    # Limpiar orden luego de pagar
    orden_actual.clear()
    return True
