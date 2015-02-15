#############################################################################
# Imports
#############################################################################

import sys
import argparse
import pkg_resources
from slidedeck import render, create

__version__ = pkg_resources.get_distribution("slidedeck").version

#############################################################################
# Functions
#############################################################################

def main():
    p = argparse.ArgumentParser(description="""
    slidedeck is a tool for creating HTML5 slideshows in markdown, based on
    the google io 2012 slidedeck. To get started and create your own slideshow,
    use the `create` command.""")
    p.add_argument(
        '-v', '--version',
        action='version',
        version = 'slidedeck %s' % __version__)


    subs = p.add_subparsers(title='command', dest='action')

    create_help='''Render a slideshow by translating the the markdown source
        into HTML5.'''
    create = subs.add_parser("create", help=create_help,
        description=create_help)
    create.add_argument('path', help='''Name of the slideshow
        to create. This will create a new directory at this path, and
        populate it with the necessary files for a skeleton slideshow.''')

    render_help = """Render a slideshow by translating the the markdown
        source into HTML5."""
    render = subs.add_parser("render", help=render_help, description=render_help)
    render.add_argument('-i', '--markdown', help='''The markdown source file.
        Default="slides.md"''', default='slides.md')
    render.add_argument('-o', '--output', help='''The outut HTML file.
        Default="index.html"''', default='index.html')
    render.add_argument('-t', '--template', help='''The template filename
        Default="base.html"''', default='base.html')


    watch_help = """Run a small process that watches the slides'
        markdown file for changes and rerenders the presentation to HTML
        whenever the slides are modified."""
    watch = subs.add_parser("watch", help=watch_help, description=watch_help)
    watch.add_argument('-i', '--markdown', help='''The markdown source file.
        Default="slides.md"''', default='slides.md')
    watch.add_argument('-o', '--output', help='''The outut HTML file.
        Default="index.html"''', default='index.html')
    watch.add_argument('-t', '--template', help='''The template filename
        Default="base.html"''', default='base.html')

    if len(sys.argv) == 1:
        # if nothing is specfied on the command line, print the help
        # text to try to be useful.
        p.parse_args(['-h'])
        sys.exit(1)

    args = p.parse_args()

    if args.action == 'render':
        render.process_slides(args.markdown, args.output, args.template)
    elif args.action == 'create':
        create.create_project(args.path)
    elif args.action == 'watch':
        # delay the import of watch until here, so that if they don't
        # have watchdog installed, the whole script won't choke
        from slidedeck import watch
        watch.watch_project(args.markdown, args.output, args.template)
    else:
        raise RuntimeError('This should never have happened')

if __name__ == '__main__':
    main()
