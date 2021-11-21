#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Определим универсальное множество

word = input("Введите слово: ")
vowels = set("a,e,i,o,u,y")
word_set = set(word.lower())
print('Гласных {} '.format(len(word_set.intersection(vowels))))




