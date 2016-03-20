# -*- coding: utf-8 -*-

import parsers


def extract(abs_path):
    dot_index = abs_path.rindex('.')
    if -1 == dot_index:
        return None
    return getattr(parsers, '%s_parser' % abs_path[dot_index:])(abs_path)