#!/usr/bin/python3.5
#coding: utf-8


import locale
locale.setlocale(locale.LC_ALL, '')
lang, encoding = locale.getlocale(locale.LC_MESSAGES)

lg = lang[0:2]

if lg not in ['en', 'fr', 'it']: lg = 'en' #For now only English, French and Italian are supported

usage = {'en': 'Usage: {x_name} [OPTION]\
OPTION can be:\
\
-v | --verbose          print debugging information during execution\
-f FILE | --file=FILE   use FILE as file to execute\
-c |--no-color          displays info in default terminal color\
-l LG | -language=LG    displays info in LG language\
-h | --help             print this message and exit\n',

         'fr': 'Usage : {x_name} [OPTION]\
OPTION peut être :\
\
-v | --verbose                affiche des informations de débogage pendant l\'exécution\
-f FICHIER | --file=FICHIER   utilise FICHIER comme script à exécuter\
-c | --no-color               affiche les informations dans la couleur par défaut du terminal\
-l LG | --language=LG         affiche les informations dans la langue LG\
-h | --help                   affiche ce message et termine\n',
         'it':'Usaggio: {x_name} [OPZIONE]\
OPZIONE può essere:\
\
-v | --verbose          stampa informazzioni di debugging durante l\'esecuzione\
-c | --no-color         stampa le informazioni nel colore predefinito del terminale\
-f FILE | --file=FILE   utilizza FILE come file a eseguire\
-l LG | --language=LG   stampa le informazioni nella lingua LG
-h | --help             stampa questo messagio e esce\n'
}

no_file = {'en': 'No such file or directory: {file}\n',
           'fr': 'Fichier ou dossier inexistant : {file}\n',
           'it': 'File o directory inesistente : {file}\n'
}

wrong_arg = {'en': 'Invalid argument: {arg}\n',
             'fr': 'Argument invalide : {arg}\n',
             'it': 'Argomento invalido : {arg}\n'
}

v_init = {'en': 'Path to file: {path}\nGrid: {grid}\n',
          'fr': 'Chemin vers le fichier : {path}\nGrille :\n{grid}\n',
          'it': 'Percorso verso la file : {path}\nGriglia :\n{grid}\n'
}

v_ip =   {'en': 'Position : {pos}\nCharacter: {char}\nDirection: {dir}\nStack    : {stack}\n\n',
            'fr': 'Position  : {pos}\nCaractère : {char}\nDirection : {dir}\nPile      : {stack}\n\n',
            'it': 'Posizione : {pos}\nCarattere : {char}\nDirezione : {dir}\nPila      : {stack}\n\n'
}

wrong_pos = {'en': 'Position: {pos} out of grid\n',
             'fr': 'Position : {pos} hors de la grille\n',
             'it': 'Posizione : {pos} fuori della griglia\n'
}

wrong_hex = {'en': '{hex} is not a valid hex number\n',
             'fr': '{hex} n\'est pas un hexadécimal valide\n',
             'it': '{hex} non è un esadecimale valido\n'
}

err_script = {'en': 'Error in script {name}\n',
              'fr': 'Erreur dans le script : {name}\n',
              'it': 'Errore nello script : {name}\n'
}

err_stack = {'en': 'Stack not empty on EOF',
             'fr': 'Pile non vide en fin de programme',
             'it': 'Pila non vuota in fine di programma'
}

end = {'en': '\nInterruption.',
       'fr': '\nInterruption.',
       'it': '\nInterruzione.'
}
