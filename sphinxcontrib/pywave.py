# We need this for older python versions, otherwise it will not use the wavedrom module
from __future__ import absolute_import

import os
from os import path
from uuid import uuid4

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Image
from sphinx.errors import SphinxError
from sphinx.ext.graphviz import figure_wrapper
from sphinx.util.fileutil import copy_asset_file
from sphinx.locale import __
from sphinx.util.docutils import SphinxDirective
from sphinx.util.i18n import search_image_for_language
from executor import sh_exec


# find the pywave tool in path
PYWAVE_CMD = "pywave -f %s -i '%s' -o '%s'"

class pywavenode(nodes.General, nodes.Inline, nodes.Element):
    """
    Special node for pywave figures
    """
    pass


class PywaveDirective(Image, SphinxDirective):
    """
    Directive to insert a wavedrom image.

    It derives from image, but is plain html when inline javascript is used.
    """
    has_content = True

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = False

    option_spec = Image.option_spec.copy()
    option_spec['caption'] = directives.unchanged
    has_content = True

    def run(self):
        filename = None
        if self.arguments:
            # Read code from file
            document = self.state.document
            if self.content:
                return [document.reporter.warning(
                    __('wavedrom directive cannot have both content and '
                       'a filename argument'), line=self.lineno)]
            argument = search_image_for_language(self.arguments[0], self.env)
            rel_filename, filename = self.env.relfn2path(argument)
            self.env.note_dependency(rel_filename)
            if not os.path.exists(filename):
                return [document.reporter.warning(
                    __('External wavedrom json file %r not found or reading '
                       'it failed') % filename, line=self.lineno)]
        else:
            # Read code from given content
            code = "\n".join(self.content)
            if not code.strip():
                return [self.state_machine.reporter.warning(
                    __('Ignoring "wavedrom" directive without content.'),
                    line=self.lineno)]
            # store into a temporary file
            filename = "tmp-%s.jsonml" % uuid4()
            with open(filename, "w+") as fp:
                fp.write(code)

        # Store code in a special docutils node and pick up at rendering
        node = pywavenode()

        node['file'] = filename
        wd_node = node # point to the actual pywave node

        # A caption option turns this image into a Figure
        caption = self.options.get('caption')
        if caption:
            node = figure_wrapper(self, wd_node, caption)
            self.add_name(node)

        # remove generated file 
        if not self.arguments:
            if os.path.exists(filename):
                os.remove(filename)
        # Run image directive processing for the options, supply dummy argument, otherwise will fail.
        # We don't actually replace this node by the image_node and will also not make it a child,
        # because intermediate steps, like converters, depend on the file being in sources. We don't
        # want to generate any files in the user sources. Store the image_node private to this node
        # and not in the docutils tree and use it later. Revisit this when the situation changes.
        self.arguments = ["dummy"]
        (wd_node['image_node'],) = Image.run(self)

        return [node]


def determine_format(supported):
    """
    Determine the proper format to render
    :param supported: list of formats that the builder supports
    :return: Preferred format
    """
    order = ['image/svg+xml', 'application/pdf', 'image/png']
    for file_format in order:
        if file_format in supported:
            return file_format
    return None

def render_pywave(self, node, outpath, bname, file_format):
    """
    Render a pywave image
    """

    # Try to convert node, raise error with code on failure
    try:
        svgout = render(node["code"])
    except JSONDecodeError as e:
        raise SphinxError("Cannot render the following json code: \n{} \n\nError: {}".format(node['code'], e))

    if not os.path.exists(outpath):
        os.makedirs(outpath)

    # SVG can be directly written and is supported on all versions
    if file_format == 'image/svg+xml':
        fname = "{}.{}".format(bname, "svg")
        fpath = os.path.join(outpath, fname)
        sh_exec(PYWAVE_CMD % ("svg", , fpath))
        return fname

    # It gets a bit ugly, if the output does not support svg. We use cairosvg, because it is the easiest
    # to use (no dependency on installed programs). But it only works for Python 3.
    try:
        import cairo
    except:
        raise SphinxError(__("Cannot import 'cairo'. In Python 2 wavedrom figures other than svg are "
                             "not supported, in Python 3 ensure 'cairo' is installed."))

    if file_format == 'application/pdf':
        fname = "{}.{}".format(bname, "pdf")
        fpath = os.path.join(outpath, fname)
        sh_exec(PYWAVE_CMD % ("cairo-pdf", , fpath))
        return fname

    if file_format == 'image/png':
        fname = "{}.{}".format(bname, "png")
        fpath = os.path.join(outpath, fname)
        sh_exec(PYWAVE_CMD % ("cairo-png", , fpath))
        return fname

    raise SphinxError("No valid wavedrom conversion supplied")


def visit_pywave(self, node):
    """
    Visit the wavedrom node
    """
    file_format = determine_format(self.builder.supported_image_types)
    if format is None:
        raise SphinxError(__("Cannot determine a suitable output format"))

    # Create random filename
    bname = "pywave-{}".format(uuid4())
    outpath = path.join(self.builder.outdir, self.builder.imagedir)

    # Render the wavedrom image
    imgname = render_pywave(self, node, outpath, bname, file_format)

    # Now we unpack the image node again. The file was created at the build destination,
    # and we can now use the standard visitor for the image node. We add the image node
    # as a child and then raise a SkipDepature, which will trigger the builder to visit
    # children.
    image_node = node['image_node']
    image_node['uri'] = os.path.join(self.builder.imgpath, imgname)
    node.append(image_node)

    raise nodes.SkipDeparture


def builder_inited(app):
    """
    Sets wavedrom_html_jsinline to False for all non-html builders for
    convenience (use ifconf etc.)
    """
    pass


def build_finished(app, exception):
    """
    When the build is finished, we copy the output image file
    to the build directory (the static folder)
    """
    # Skip for non-html
    if app.config.pywave_html:
        return
    # for others move image into _static folder
    #copy_asset_file(path.join(app.builder.srcdir, app.config.offline_wavedrom_js_path), path.join(app.builder.outdir, '_static'), app.builder)

def setup(app):
    """
    Setup the extension
    """
    app.add_config_value('pywave_html', True, 'html')
    app.add_directive('pywave', PywaveDirective)
    app.connect('build-finished', build_finished)
    app.connect('builder-inited', builder_inited)

    app.add_node(pywavenode,
                 html = (visit_pywave, None),
                 latex = (visit_pywave, None),
                 )

