# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#  License: LICENSE.TXT
#
#  Copyright (c) 2011-14, Enthought, Inc.
#  All rights reserved.
# -----------------------------------------------------------------------------
from sectiondoc.util import fix_backspace, NEW_LINE


def rubric(doc, header, renderer=None, item_class=None):
    """ Refactor a header section using the rubric directive.

    The method supports refactoring of single word headers, two word headers
    and headers that include a backslash ''\''.

    Arguments
    ---------
    header : string
        The header string to use with the rubric directive.

    """
    header = fix_backspace(header)
    directive = '.. rubric:: {0}'.format(header)
    return [directive, NEW_LINE]
