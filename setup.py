"""Slidedeck: Kickass-beautiful HTML5 slides in markdown

This is a repackaging of the google io 2012 slidedeck,
to be a little easier to use and more suitable for scientific
presentations.

Example slides: http://cdn.rawgit.com/rmcgibbo/slidedeck-example/master/index.html

You edit and author your entire presentation in markdown. All the metadata
about your presentation is set within the markdown file, including things
like the title and author. You run `slidedeck create` to make a new deck.
This will create a new directory with your project. In particular, there will
be a fine in there called slides.md that contains the markdown source for
your slides. `slidedeck render` will render your deck from markdown to html5.
`slidedeck watch` will watch your project and rerender the slides whenever
you change the content (useful for iterative development).
"""

DOCLINES = __doc__.split("\n")

from setuptools import setup, find_packages

CLASSIFIERS = """\
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
License :: Public Domain
Programming Language :: Python
Operating System :: OS Independent
Topic :: Internet :: WWW/HTTP
"""

setup(
    name='slidedeck',
    version='0.14',
    author='Robert McGibbon',
    author_email='rmcgibbo@gmail.com',
    url='https://github.com/rmcgibbo/slidedeck',
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    classifiers = CLASSIFIERS.splitlines(),
    packages=find_packages(),
    entry_points={'console_scripts': ['slidedeck=slidedeck.scripts.slidedeck:main']},
    platforms = ["Linux", "Mac OS-X", "Unix"],
    package_data={'slidedeck': ['data/base.html', 'data/slides.md',
                    'data/js/*.js', 'data/js/*/*.js', 'data/theme/*/*',
                    'data/figures/*']},
    zip_safe=False,
    install_requires=['jinja2', 'markdown', 'watchdog'],
)
