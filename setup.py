from setuptools import setup

setup(
    name='slidedeck',
    packages=['slidedeck'],
    scripts=['scripts/slidedeck'],
    package_data={'slidedeck': ['data/base.html', 'data/slides.md',
                    'data/js/*.js', 'data/js/*/*.js', 'data/theme/*/*',
                    'data/figures/*']},
    zip_safe=False,
)
