This repo holds the files for a presentation I gave for Notre Dame Summer Scholars 2011.

The bulk of the content is in presentation.rst.

The final slide output, using s5, is in presentation.html, which uses the accompanying ui directory to function properly.

Output can be rendered with sphinx, using the Makefile, or docutils using rst2s5.py


Generating solution RST files
=============================
If you create a new solution, the output can be created like so::
       
        $ python transfer_exercises_to_rst.py

The files will then be stored in the solutions/ directory


Generating PDF output
=====================
Run the following command::

        $ make pdflatex


Generating S5 Slide Output
==========================
Run the following command::

        $ python rst2s5.py presentation.rst > presentation.html

Also, make sure you edit the generated title tags.  Also, you can update the theme by editing this line::
       
        <link rel="stylesheet" href="ui/default/slides.css"
              type="text/css" media="projection" id="slideProj" />

Change ``i18n`` to the name of your desired template.
