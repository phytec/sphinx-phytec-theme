sphinx-phytec-theme
===================

PHYTEC Sphinx theme (based on ``sphinx-rtd-theme``) and extensions, used by
the PHYTEC documentation at https://github.com/phytec/doc-bsp-yocto.

Installing ``sphinx-phytec-theme`` automatically installs
``sphinx-rtd-theme``.

Usage
-----

Install a tagged release::

   pip install "sphinx-phytec-theme @ git+https://github.com/phytec/sphinx-phytec-theme.git@v0.1.0"

Enable it in ``conf.py``::

   extensions = [
       'sphinx_phytec_theme',
   ]
   html_theme = 'sphinx_phytec_theme'

The extension:

- registers the ``sphinx_phytec_theme`` HTML theme (inherits ``sphinx_rtd_theme``),
- provides default logo, favicon, ``robots.txt`` and stylesheet,
- provides the language selector template (``versions.html``),
- enables the ``custom_sectnum`` extension (``sectnum`` directive that does
  not number the uppermost section title).

Any ``html_logo`` or ``html_favicon`` set in ``conf.py`` takes precedence.

Language selector
-----------------

Set ``languages`` in ``html_context``::

   html_context = {
       'languages': [
           ['en', 'https://example.com'],
           ['zh_CN', 'https://example.com/zh_CN'],
       ]
   }

Development
-----------

::

   pip install -e .
   python -m build

Releases are tagged ``vX.Y.Z``.
