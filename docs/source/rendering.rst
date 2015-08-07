Docstring rendering
*******************

The are five different parts in the pipeline of **sectiondoc** docstring rendering.

Style
#####

The rendering :class:`~Style` is hooked with autodoc to receive the docstring
of the various objects and maps the objects types provided by autodoc to
:class:`~DocRender` instances which are responsible for rendering the provided
docstring.

The DocRender
#############

The DocRender is responsible for doing the actual work. At initialization
The class receives a dictionary mapping sections to a rendering function
and optional section item parsing and rendering classes. The actual
rendering starts by executing :meth:`~.DocRender.parse` to detect sections
in the docstring. For each section that is discovered the
:meth:`~.DocRender._render` is called with the name of the discovered section
to further dispatch processing to the associated section rendering function.
If a associated fuctntion to the section does not exist the default is to use
:func:`~.rubric`.

Section rendering function
##########################

The rendering fuctions is will use the utility methods of the the DocRender
instance to extract the section block. Depedending on the implementation
:meth:`~DocRender.extract_paragraph` will call to return the
paragraph for further processing or will call
:meth:`~DocRender.extract_items` to return the list of :class:`~.Item`
instances. After collecting the information in the section the rendering
function is ready to produce the updated rst using the appropriate
:class:`~.Renderer` and return a list of lines that will be re-inserted into
the docstring.

Item
####

:class:`Item` instances contain the ``term``, ``classfier(s)`` and
``definition`` information of items in a section. Each :class:`Item` type
knows how to parse a set of lines grouping and filtering the information
ready to ber rendered inot sphinx friendly rst.

Renderer
########

The :class:`Renderer` is used by the section renderer functions to render
a previously contructed :class:`Item` into sphinx friently rst.