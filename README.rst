CobraIDE
========

CobraIDE is a portable IDE for **COBOL** (GnuCOBOL), **Python**, **MicroPython**
and **CircuitPython**, for Windows. It is derived from OpenCobolIDE 4.7.6
(https://github.com/OpenCobolIDE/OpenCobolIDE, no longer maintained since 2018).
The Python package is still called ``open_cobol_ide``.

*CobraIDE est un environnement de développement portable pour le COBOL
(GnuCOBOL), le Python, le MicroPython et le CircuitPython, sous Windows. Son
interface est en français par défaut (variable d'environnement* ``OCIDE_LANG=en``
*pour l'anglais).*


Download
--------

Get the latest ``CobraIDE-<version>-win64.zip`` from the **Releases** page:
https://github.com/GillesBart/CobraIDE/releases

Unzip it anywhere (a USB drive works too) and run ``CobraIDE.exe``. Nothing is
installed: the settings are kept in the ``data`` folder next to the program, and
everything is found again when a removable drive changes its drive letter.


Features
--------

COBOL

- syntax highlighting, code completion, code folding, navigable tree of
  divisions, sections and paragraphs
- tool for computing PIC fields offsets
- compile and run from the editor (GnuCOBOL 3.2 is bundled)

Python, MicroPython and CircuitPython

- editor with outline, auto-indentation and live syntax checking
- run the program from the editor
- **Board panel** (button *Board* of the file system dock): browse the files of
  a MicroPython or CircuitPython board, open them, edit them and save them back
  to the board; create, rename and delete files and folders. Boards are
  recognised by their USB serial number. A CircuitPython board mounted as a
  USB drive (CIRCUITPY) is edited directly; other boards go through
  ``mpremote`` (installed from the MicroPython menu).

Editing

- tabs: double-click a tab to close it (a modified file asks to be saved),
  double-click the free space of the tab bar for a new document
- drag and drop files on the editor to open them
- file encodings can be changed from the context menu
- dark color schemes and theme


Running from the sources
------------------------

Python 3.13 is used. In the CobraIDE folder::

    py -3.13 -m venv .venv
    .venv\Scripts\activate
    pip install PyQt5 pygments pywin32 cx_Freeze
    set PYTHONPATH=%CD%\open_cobol_ide\extlibs;%CD%
    python CobraIDE.pyw

Building ``CobraIDE.exe`` (cx_Freeze), with the same ``PYTHONPATH``::

    rmdir /s /q build
    cd scripts
    python freeze.py


License
-------

CobraIDE is released under the **GPL** version 3, like OpenCobolIDE. See
``LICENSE`` and ``AUTHORS.rst`` for the credits of the original project.
