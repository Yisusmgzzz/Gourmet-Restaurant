#!/usr/bin/env python3
# main.py
# NOMBRES DE LOS INTEGRANTES DEL PROYECTO:
# JESUS ESTEBAN MUNOZ GOMEZ
# ALBEIRO ANDRES RODGERS PEREZ
# ALEX JAVIER CAMPO SUAREZ

import titles as t
import menu as m
import restaurant as rt
import crud_restaurante as cr
import i18n


def menu_pedidos_categoria(categoria_nombre):
    """Muestra los platos de una categoria y permite seleccionar plato y cantidad."""
    disponibles = m.mostrar_categoria(categoria_nombre)
    if not disponibles:
        input(i18n.tr("press_enter_back"))
        return

    while True:
        cod = input(i18n.tr("enter_code")).strip()
        if cod == "0":
            break

        if cod not in m.PLATOS or m.PLATOS[cod]["categoria"] != categoria_nombre:
            print(i18n.tr("invalid_code_cat"))
            continue

        plato_sel = m.PLATOS[cod]
        nombre_sel = i18n.dish_name(cod, plato_sel["nombre"])
        precio_fmt = f"${plato_sel['precio']:,}".replace(",", ".")
        print(i18n.tr("selected", name=nombre_sel, price=precio_fmt))
        
        try:
            cant = int(input(i18n.tr("enter_qty")).strip())
            if cant <= 0:
                print(i18n.tr("qty_gt_zero"))
                continue
        except ValueError:
            print(i18n.tr("qty_int"))
            continue

        exito, msg = rt.agregar_producto(cod, cant)
        print(f"\n>> {msg}")

        seguir = input(i18n.tr("add_more")).strip()
        if not i18n.is_yes(seguir):
            break


def menu_administrador():
    """Submenú de Gestión y Operaciones CRUD con la base de datos PostgreSQL."""
    while True:
        t.limpiar_pantalla()
        print("=" * 50)
        print("    PANEL DE ADMINISTRACIÓN Y BASE DE DATOS    ")
        print("=" * 50)
        estado_bd = cr.obtener_estado_conexion()
        print(f" Estado: [{estado_bd}]")
        print("-" * 50)
        print("1. Registrar nuevo plato (INSERT)")
        print("2. Consultar plato específico (SELECT)")
        print("3. Consultar todos los platos en PostgreSQL (SELECT)")
        print("4. Actualizar información de un plato (UPDATE)")
        print("5. Retirar plato de la carta (DELETE)")
        print("6. Reintentar conexión a PostgreSQL")
        print("0. Volver al Menú Principal")
        print("=" * 50)

        op = input("Seleccione una opción (0-6): ").strip()
        if op == "1":
            cr.registrar_plato()
            input("\nPresione ENTER para continuar...")
        elif op == "2":
            cr.consultar_plato()
            input("\nPresione ENTER para continuar...")
        elif op == "3":
            cr.consulta_todos_platos()
            input("\nPresione ENTER para continuar...")
        elif op == "4":
            cr.actualiza_plato()
            input("\nPresione ENTER para continuar...")
        elif op == "5":
            cr.eliminar_plato()
            input("\nPresione ENTER para continuar...")
        elif op == "6":
            cr.conectar_bd()
            if cr.esta_conectado():
                cr.sincronizar_con_menu()
                print("¡Conectado exitosamente y menú sincronizado con la base de datos!")
            else:
                print("No se pudo conectar a PostgreSQL.")
            input("\nPresione ENTER para continuar...")
        elif op == "0":
            break
        else:
            print("Opción no válida.")
            input("\nPresione ENTER para continuar...")


def main():
    # Establecer conexion con PostgreSQL (con autodeteccion y respaldo local si no esta disponible)
    conectado = cr.conectar_bd()
    if conectado:
        cr.sincronizar_con_menu()

    t.limpiar_pantalla()
    t.banner_bienvenida()

    # Confirmacion de ingreso al sistema
    ingresar = input(i18n.tr("ask_enter")).strip()
    if not i18n.is_yes(ingresar):
        print(i18n.tr("bye_visit"))
        return

    while True:
        estado_bd = cr.obtener_estado_conexion()
        print("\n" + "=" * 45)
        print(i18n.tr("main_title"))
        print(f"       [{estado_bd}]")
        print("=" * 45)
        print(i18n.tr("opt_breakfast"))
        print(i18n.tr("opt_lunch"))
        print(i18n.tr("opt_dessert"))
        print(i18n.tr("opt_view_order"))
        print(i18n.tr("opt_invoice"))
        print(i18n.tr("opt_cancel"))
        print(i18n.tr("opt_admin"))
        print(i18n.tr("opt_lang"))
        print(i18n.tr("opt_exit"))
        print("=" * 45)

        opcion = input(i18n.tr("select_option")).strip()

        match opcion:
            case "1":
                t.limpiar_pantalla()
                menu_pedidos_categoria("Desayuno")
            case "2":
                t.limpiar_pantalla()
                menu_pedidos_categoria("Almuerzo")
            case "3":
                t.limpiar_pantalla()
                menu_pedidos_categoria("Postre")
            case "4":
                t.limpiar_pantalla()
                rt.ver_orden()
                input(i18n.tr("press_enter"))
            case "5":
                t.limpiar_pantalla()
                if not rt.orden_actual:
                    print(i18n.tr("order_empty"))
                    input(i18n.tr("press_enter"))
                else:
                    cliente = input(i18n.tr("enter_name")).strip()
                    if not cliente:
                        cliente = i18n.tr("default_customer")
                    rt.generar_factura(cliente)
                    input(i18n.tr("press_enter"))
            case "6":
                rt.cancelar_orden()
                input(i18n.tr("press_enter"))
            case "7":
                menu_administrador()
            case "8":
                i18n.toggle_lang()
                print(i18n.tr("lang_changed"))
                input(i18n.tr("press_enter"))
            case "0":
                cr.terminar()
                print(i18n.tr("goodbye"))
                break
            case _:
                print(i18n.tr("invalid_option"))


if __name__ == "__main__":
    main()
