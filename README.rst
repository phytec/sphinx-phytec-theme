sphinx-phytec-theme
===================

PHYTEC Sphinx theme (based on ``sphinx-rtd-theme``) and extensions, used by the
PHYTEC documentation at https://github.com/phytec/doc-bsp-yocto.

Installing ``sphinx-phytec-theme`` automatically installs ``sphinx-rtd-theme``.

Usage
-----

Install a tagged release::

   pip install "sphinx-phytec-theme @ git+https://github.com/phytec/sphinx-phytec-theme.git@0.5.0"

Enable it in ``conf.py``::

   extensions = [
       'sphinx_phytec_theme',
   ]
   html_theme = 'sphinx_phytec_theme'

The extension:

- registers the ``sphinx_phytec_theme`` HTML theme (inherits
  ``sphinx_rtd_theme``),
- provides default logo, favicon, ``robots.txt`` and stylesheet,
- provides the language selector template (``versions.html``),
- enables the ``custom_sectnum`` extension (``sectnum`` directive that does not
  number the uppermost section title),
- enables the ``badges`` extension (inline badge roles, see below).

Any ``html_logo`` or ``html_favicon`` set in ``conf.py`` takes precedence.

Badges
------

The ``badges`` extension provides inline roles, e.g. for documenting option
metadata::

   ``api-version`` :badge-type:`integer` :badge-state:`required` :badge-since:`0.1.0`

- ``:badge:`` generic badge
- ``:badge-type:`` type badge (prefixed with "Type:")
- ``:badge-state:`` state badge; ``required``, ``optional``, ``deprecated`` and
  ``experimental`` have their own colors
- ``:badge-since:`` version badge (prefixed with "Since:")

To link the since badge to a release notes section, set a template in
``conf.py``. ``{version}`` is replaced by the version and the result is used as
a ``:ref:`` target::

   badges_release_notes_ref = 'release-{version}'

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

Releases are tagged ``X.Y.Z`` (without a leading ``v``).
