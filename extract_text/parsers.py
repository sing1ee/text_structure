# -*- coding: utf-8 -*-

import textract
import functools

pdf_parser = functools.partial(textract.process, method='pdfminer', encoding='utf_8')
doc_parser = functools.partial(textract.process, method='doc', encoding='utf_8')
docx_parser = functools.partial(textract.process, method='docx', encoding='utf_8')
html_parser = functools.partial(textract.process, method='html', encoding='utf_8')