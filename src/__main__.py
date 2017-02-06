import sys
import io
import CommonMark
from github_markdown_css import GITHUB_MARKDOWN_CSS

DOCUMENT_TEMPLATE = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<title>{title}</title>
<style type="text/css">code{{white-space: pre;}}</style>
<style>
{github_markdown_css}
</style>
<style>
.markdown-body {{
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
}}
</style></head><body class="markdown-body">
{body}
</body></html>
"""

input_filename = sys.argv[1]
title = sys.argv[2]
output_filename = sys.argv[3]

parser = CommonMark.Parser()
renderer = CommonMark.HtmlRenderer()
with io.open(input_filename, encoding = 'utf-8') as f:
    md = f.read()
ast = parser.parse(md)
body = renderer.render(ast)
with io.open(output_filename, 'w', encoding = 'utf-8') as f:
    f.write(DOCUMENT_TEMPLATE.format(title = title, github_markdown_css = GITHUB_MARKDOWN_CSS, body = body))
