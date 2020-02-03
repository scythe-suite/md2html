import sys
from pathlib import Path

import markdown
from github_markdown_css import GITHUB_MARKDOWN_CSS

DOCUMENT_TEMPLATE = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<title>{title}</title>
<style>
{github_markdown_css}
/* md2html specific */
.markdown-body {{
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
}}
code {{
  white-space: pre-wrap !important;
  }}
</style></head><body class="markdown-body">
{body}
</body></html>
"""

VERSION = '1.1.1'

input_filename = sys.argv[1]

if input_filename == 'version':
  sys.stderr.write('Version: {}\n'.format(VERSION))
  sys.exit()

title = sys.argv[2]
output_filename = sys.argv[3]

body = markdown.markdown(Path(input_filename).read_text(), extensions = ['pymdownx.b64'])
Path(output_filename).write_text(DOCUMENT_TEMPLATE.format(title = title, github_markdown_css = GITHUB_MARKDOWN_CSS, body = body))