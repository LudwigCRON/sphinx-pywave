Sphinx pywave extension 
=========================

A sphinx extension that allows including pywave diagrams by using its text-based representation

pywave online editor and tutorial: http://pywave.com/

.. image:: https://travis-ci.org/LudwigCRON/sphinx-pywave.svg?branch=master
	:target: https://travis-ci.org/LudwigCRON/sphinx-pywave


Installation
------------

The pywave extension can be installed using pip:

::

	pip install sphinxcontrib-pywave

and by adding **'sphinxcontrib.pywave'** to the extensions list in your conf.py file.

Directives
----------

The extension is useable in the form of an extra pywave directive, as shown below.

::

	.. pywave::

		{ "signal": [
		  	{ "name": "clk",  "wave": "P......" },
		  	{ "name": "bus",  "wave": "x.==.=x", "data": ["head", "body", "tail", "data"] },
		  	{ "name": "wire", "wave": "0.1..0." }
		]}

Alternatively, it can read the json from a file:

::

	.. pywave:: mywave.json

When configured to generate images (see `Configuration`_) the directive will generate an image and include
it into the input. It allows for the same configuration as the image directive:

::

	.. pywave:: mywave.json
        :height: 100px
        :width: 200 px
        :scale: 50 %
        :alt: alternate text
        :align: right

The image can be turned into a figure by adding a caption:

::

    .. pywave:: mywave.json
        :caption: My wave figure

The extension can be configured (see `Configuration`_) to not generate an image out of the diagram description
itself, but to surround it with some html and js tags in the final html document that allow the images to be rendered
by the browser. This is the currently the default for HTML output.

Examples
--------

In the `example` folder, you can find a couple of examples (taken from the pywave tutorial), illustration the use of the extension.
