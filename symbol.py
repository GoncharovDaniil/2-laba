#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = input("Введите первое множество: ")
b = input("Введите второе множество: ")
unique = set(a).intersection(b)
print("Количество общих символов: ", len(unique))
print("Общие символы:", unique)



