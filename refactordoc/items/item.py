﻿import abc
from collections import namedtuple


class Item(namedtuple('Item', ['term', 'classifiers', 'definition'])):
    """ A docstring item.

    The Item class is responsible to check, parse and refactor a docstring
    item into sphinx friendly rst.

    Syntax diagram:

        +-------------------------------------------------+
        | header                                          |
        +--+----------------------------------------------+---+
           | definition                                       |
           | (body elements)+                                 |
           +--------------------------------------------------+


    Depending only the type of the list item the header is split into a
    term and one or more classifiers.

    Attributes
    ----------
    term : str
        The term usually reflects the name of a parameter or an attribute.

    classifiers: list
        The classifier(s) of the term. Commonly used to reflect the type
        of an argument or the signature of a function.

    definition : list
        The list of strings that holds the description the definition item.

    """

    @property
    def mode(self):
        """ The operational mode of the item based on the available info.
        """
        if self.classifiers == [] and self.definition == ['']:
            mode = 'only_term'
        elif self.classifiers == []:
            mode = 'no_classifiers'
        elif self.definition == ['']:
            mode = 'no_definition'
        else:
            mode = 'full'
        return mode

    @classmethod
    def is_item(cls, line):
        """ Check if the line is describing an item.

        The method is used to check that a line is following the expected
        format for the term and classifiers attributes.

        """
        raise NotImplementedError()

    @classmethod
    def parse(cls, lines):
        """Parse a definition item from a set of lines.

        The class method parses the item from the list of docstring lines and
        produces a DefinitionItem with the term, classifier and the definition.

        .. note:: The global indention in the definition lines is striped

        Arguments
        ---------
        lines :
            docstring lines of the definition without any empty lines before or
            after.

        Returns
        -------
        item : Item

        """
        raise NotImplementedError()
