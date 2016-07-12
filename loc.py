#!/usr/bin/python3.5
#coding: utf-8


import locale
locale.setlocale(locale.LC_ALL, "")
_user_lang, _user_coding = locale.getlocale(locale.LC_MESSAGES)

if 'en' in _user_lang: raise ImportError

_lg = _user_lang[0:2]

_no_file__en = 'No such file or directory: '
_no_file__fr = 'Fichier ou dossier inexistant : '

_wrong_arg__en = 'Invalid argument: '
_wrong_arg__fr = 'Argument invalide : '
_wrong_arg__it = 'Argomento invalido : '

_v_path__en = 'Path: '
_v_path__fr = 'Chemin : '
_v_path__it = 'Camino : '

_v_grid__en = 'Grid: '
_v_grid__fr = 'Grille : '
_v_grid__it = 'Griglia : '

_v_pos__en = 'Position: '
_v_pos__fr = 'Position : '
_v_pos__it = 'Posizione : '

_v_char__en = 'Character: '
_v_char__fr = 'Caractère : '
_v_char__it = 'Carattere : '

_v_stack__en = '\nStack: '
_v_stack__fr = '\nPile : '
_v_stack__it = '\nPila : '

_wrong_hex__en = ' is not a valid hex number\n'
_wrong_hex__fr = ' n\'est pas un hexadécimal valide\n'
_wrong_hex__it = ' non è un esadecimale valido\n'

_err_script__en = 'Error in script: '
_err_script__fr = 'Erreur dans le script : '
_err_script__it = 'Errore nello script : '

_quit__en = '\nInterruption.'
_quit__fr = '\nInterruption.'
_quit__it = '\nInterruzione.'

msg = {'no_file': '', 'wrong_arg':'', 'v_path': '', 'v_grid': '', 'v_pos': '', 'v_char': '', 'v_stack': '', 'wrong_hex': '', 'err_script': '', 'quit': ''}
for k in msg:
    try:
        msg[k] = eval('_' + k + '__' + _lg)
    except NameError:
        msg[k] = eval('_' + k + '__en')
