from esp_docs.conf_docs import *  # noqa: F403,F401

languages = ['en', 'zh_CN']

extensions += ['sphinx_copybutton',
               'sphinxcontrib.wavedrom',
               ]

# Disable format_esp_target
extensions.remove('esp_docs.esp_extensions.format_esp_target')

# Use wavedrompy as backend, instead of wavedrom-cli
render_using_wavedrompy = True

# link roles config
project_homepage = 'https://github.com/espressif/esp-faq'
github_repo = 'espressif/esp-faq'

# Context used by sphinx_idf_theme
html_context['github_user'] = 'espressif'
html_context['github_repo'] = 'esp-faq'

html_static_path = ['../_static']

# add Tracking ID for Google Analytics
google_analytics_id = 'G-1SP3XY5NKQ'

# Extra options required by sphinx_idf_theme
project_slug = 'esp-faq'

# Final PDF filename will contains target and version
pdf_file_prefix = u'esp-faq'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

linkcheck_exclude_documents = ['index',  # several false positives due to the way we link to different sections
                               ]
