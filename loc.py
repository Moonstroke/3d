#!/usr/bin/python3.5
#coding: utf-8


import locale
locale.setlocale(locale.LC_ALL, "")
language, encoding = locale.getlocale(locale.LC_MESSAGES)

if 'en' in language: raise ImportError

lg = language[0:2]

no_file__en = 'No such file or directory: '
no_file__fr = 'Fichier ou dossier inexistant : '


wrong_arg__en = 'Invalid argument: '
wrong_arg__fr = 'Argument invalide : '
wrong_arg__it = 'Argomento invalido : '

v_path__en = 'Path: '
v_path__fr = 'Chemin : '
v_path__it = 'Camino : '

v_grid__en = 'Grid: '
v_grid__fr = 'Grille : '
v_grid__it = 'Griglia : '

v_pos__en = 'Position: '
v_pos__fr = 'Position : '
v_pos__it = 'Posizione : '

v_char__en = 'Character: '
v_char__fr = 'Caractère : '
v_char__it = 'Carattere : '

v_stack__en = '\nStack: '
v_stack__fr = '\nPile : '
v_stack__it = '\nPila : '

wrong_hex__en = ' is not a valid hex number\n'
wrong_hex__fr = ' n\'est pas un hexadécimal valide\n'
wrong_hex__it = ' non è un esadecimale valido\n'

err_script__en = 'Error in script: '
err_script__fr = 'Erreur dans le script : '
err_script__it = 'Errore nello script : '

quit__en = '\nInterruption.'
quit__fr = '\nInterruption.'
quit__it = '\nInterruzione.'

msg = {'no_file': '', 'wrong_arg':'', 'v_path': '', 'v_grid': '', 'v_pos': '', 'v_char': '', 'v_stack': '', 'wrong_hex': '', 'err_script': '', 'quit': ''}
for k in msg:
    try:
        msg[k] = eval(k + '__' + lg)
    except NameError:
        msg[k] = eval(k + '__en')
