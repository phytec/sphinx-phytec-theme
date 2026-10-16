"""PHYTEC Sphinx theme and extensions."""

from importlib.metadata import PackageNotFoundError, version as _version
from pathlib import Path

try:
    __version__ = _version('sphinx-phytec-theme')
except PackageNotFoundError:  # pragma: no cover
    __version__ = '0.0.0'

_THEME_DIR = Path(__file__).parent / 'theme'
_STATIC_DIR = _THEME_DIR / 'phytec' / 'static'


def _config_inited(app, config):
    """Set defaults without overriding values set by the user."""
    if not config.html_logo:
        config.html_logo = str(_STATIC_DIR / 'logo-phytec.svg')
    if not config.html_favicon:
        config.html_favicon = str(_STATIC_DIR / 'favicon.ico')
    config.html_extra_path = list(config.html_extra_path) + [
        str(_STATIC_DIR / 'robots.txt')
    ]


def setup(app):
    app.setup_extension('sphinx_rtd_theme')
    app.setup_extension('sphinx_phytec_theme.custom_sectnum')
    app.setup_extension('sphinx_phytec_theme.badges')
    app.add_html_theme('sphinx_phytec_theme', str(_THEME_DIR / 'phytec'))
    app.add_css_file('css/phytec-theme.css')
    app.connect('config-inited', _config_inited)
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
