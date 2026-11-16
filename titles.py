#!/usr/bin/env python3
# titles.py
# Modulo con los encabezados y titulos del restaurante

import i18n


def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def banner_bienvenida():
    print("=" * 45)
    print("        RESTAURANTE GOURMET        ")
    print(i18n.tr("welcome"))
    print("=" * 45)


def breakfast_menu():
    print("\n" + "=" * 40)
    print(i18n.tr("header_breakfast"))
    print("=" * 40)


def midfood_menu():
    print("\n" + "=" * 40)
    print(i18n.tr("header_lunch"))
    print("=" * 40)


def desserts_menu():
    print("\n" + "=" * 40)
    print(i18n.tr("header_dessert"))
    print("=" * 40)


def factura_header():
    print("\n" + "=" * 45)
    print(i18n.tr("invoice_summary"))
    print("=" * 45)
