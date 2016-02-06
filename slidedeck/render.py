"""Code to convert the markdown source into the final HTML output
"""

import os
from collections import defaultdict
import codecs
import re
import jinja2
import markdown
from slidedeck.mdx_mathjax import MathJaxExtension

#############################################################################
# Globals
#############################################################################

# these are a set of regular expressions that are looked for in the markdown
# that provide metadata about the slide deck and are used to populate the
# title slide (at the beginning) and thank you slide (at the end)
#
# lines in the markdown that look like:
#
# % author: FirstName LastName
#
# Will be detected.
DECK_SETTINGS_RE = {
    'thankyou': u'^%\s*thankyou:(.*)$',
    'thankyou_details': u'^%\s*thankyou_details:(.*)$',
    'title': u'^%\s*title:(.*)$',
    'subtitle': u'^%\s*subtitle:(.*)$',
    'author': u'^%\s*author:(.*)$',
    'contact': u'^%\s*contact:(.*)$',
    'favicon': u'^%\s*favicon:(.*)$',

}

#############################################################################
# Functions related to the render command
#############################################################################


def render_slides(md, template_fn):

    md, settings = parse_deck_settings(md)
    md_slides = md.split('\n---\n')
    print("Compiled {:d} slides.".format(len(md_slides)))

    slides = []
    # Process each slide separately.
    for md_slide in md_slides:
        slide = {}
        sections = md_slide.split('\n\n')
        # Extract metadata at the beginning of the slide (look for key: value)
        # pairs.
        metadata_section = sections[0]
        metadata = parse_metadata(metadata_section)
        slide.update(metadata)
        remainder_index = metadata and 1 or 0
        # Get the content from the rest of the slide.
        content_section = '\n\n'.join(sections[remainder_index:])
        html = markdown.markdown(content_section, extensions=[MathJaxExtension()])
        slide['content'] = postprocess_html(html, metadata)

        slides.append(slide)

    template = jinja2.Template(open(template_fn).read())
    return template.render(locals())


def write_slides(slidestring, output_fn):
    with codecs.open(output_fn, 'w', encoding='utf8') as outfile:
        outfile.write(slidestring)


def process_slides(markdown_fn, output_fn, template_fn):
    if not os.path.exists(markdown_fn):
        raise OSError('The markdown file "%s" could not be found.' % markdown_fn)
    md = codecs.open(markdown_fn, encoding='utf8').read()

    # Check for Dos\Windows line encoding \r\n and convert to unix style \n
    if '\r\n' in md:
        md = md.replace('\r\n', '\n')

    slides = render_slides(md, template_fn)
    write_slides(slides, output_fn)



def parse_deck_settings(md):
    """Parse global settings for the slide deck, such as the author and
    contact information.

    Parameters
    ----------
    md : unicode
        The full markdown source of the slides

    Returns
    -------
    md : unicode
        The markdown source, after the settings have been removed, such
        that they don't get actually put into the slides directly
    settings : dict
        A dict containing the settings. The keys wil be the set of keys
        in DECK_SETTINGS_RE, modulo the keys that were actually parsed
        from the document.
    """
    settings = defaultdict(lambda: [])
    for key, value in DECK_SETTINGS_RE.items():
        found = True
        while found:
            m = re.search(value, md, re.MULTILINE)
            if m:
                settings[key].append(m.group(1))
                md = md.replace(m.group(0), '')
            else:
                found = False

    # if a setting is repeated, we join them together with a <br/> tag
    # in between.
    settings = {k: '<br/>'.join(v) for k, v in settings.items()}

    print("Parsed slide deck settings, and found setting for: {:s}.".format(', '.join(settings.keys())))
    # strip off the newline characters at the beginning and end of the document
    # that might have been left
    md = md.strip()
    return md, settings


def parse_metadata(section):
    """Given the first part of a slide, returns metadata associated with it."""
    metadata = {}
    metadata_lines = section.split('\n')
    for line in metadata_lines:
        colon_index = line.find(':')
        if colon_index != -1:
            key = line[:colon_index].strip()
            val = line[colon_index + 1:].strip()
            metadata[key] = val

    return metadata


def postprocess_html(html, metadata):
    """Returns processed HTML to fit into the slide template format."""
    if metadata.get('build_lists') and metadata['build_lists'] == 'true':
        html = html.replace('<ul>', '<ul class="build">')
        html = html.replace('<ol>', '<ol class="build">')
    return html
