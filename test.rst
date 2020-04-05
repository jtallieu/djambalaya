
::

DEMO
====

Playing with code
----

.. code:: python
   
   class Attr(object):
      name = "not set"

.. code:: javascript
   
   var load = function(){
       var i = 20;
       var timer = window.setInterval(function(){
           console.log("boo");
       }, 1000);
   }()

Done.


=====================================================
 The reStructuredText_ Cheat Sheet: Syntax Reminders
=====================================================
:Info: See <http://docutils.sf.net/rst.html> for introductory docs.
:Author: David Goodger <goodger@python.org>
:Date: $Date: 2013-02-20 02:10:53 +0100 (Mi, 20. Feb 2013) $
:Revision: $Revision: 7612 $
:Description: This is a "docinfo block", or bibliographic field list

.. NOTE:: If you are reading this as HTML, please read
   `<cheatsheet.txt>`_ instead to see the input syntax examples!

Section Structure
=================
Section titles are underlined or overlined & underlined.

Body Elements
=============
Grid table:

+--------------------------------+-----------------------------------+
| Paragraphs are flush-left,     | Literal block, preceded by "::":: |
| separated by blank lines.      |                                   |
|                                |     Indented                      |
|     Block quotes are indented. |                                   |
+--------------------------------+ or::                              |
| >>> print 'Doctest block'      |                                   |
| Doctest block                  | > Quoted                          |
+--------------------------------+-----------------------------------+
| | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
| |     Useful for addresses, verse, and adornment-free lists; long  |
|       lines can be wrapped with continuation lines.                |
+--------------------------------------------------------------------+

Simple tables:

================  ============================================================
List Type         Examples (syntax in the `text source <cheatsheet.txt>`_)
================  ============================================================
Bullet list       * items begin with "-", "+", or "*"
Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
                  #. also auto-enumerated
Definition list   Term is flush-left : optional classifier
                      Definition is indented, no blank line between
Field list        :field name: field body
Option list       -o  at least 2 spaces between option & description
================  ============================================================

================  ============================================================
Explicit Markup   Examples (visible in the `text source`_)
================  ===============================
