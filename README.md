Slidedeck: HTML5 Slideshows in markdown
---------------------------------------
[![PyPI Version](https://badge.fury.io/py/slidedeck.png)](https://pypi.python.org/pypi/slidedeck)
[![Downloads](https://pypip.in/d/slidedeck/badge.png)](https://pypi.python.org/pypi/slidedeck)

### [Take a look at these slides!](http://rawgit.com/rmcgibbo/slidedeck-example/master/index.html)


Overview
========

This is a repackaging of the google io 2012 slidedeck, with [some](https://github.com/francescolaffi/elastic-google-io-slides) modifications, to be a little easier to use and more suitable for scientific presentations.

We've made a few changes:

- You edit and author your entire presentation in markdown.
- All the metadata about your project is set within the markdown file, including things like
  the title and author.
- It's packaged as a python project.
    - You run `slidedeck create` to make a new deck. This will create a new directory with your
      project. In particular, there will be a fine in there called `slides.md` that contains the
      markdown source for your slides.
    - `slidedeck render` will render your deck from markdown to html5.
    - `slidedeck watch` will watch your project and rerender the slides whenever you change the
       content (useful for iterative development).
- I made a few stylistic changes to the css, including changing the font size.
- The slides can contain LaTeX, which is rendered via mathjax.
- There are no google logos all over the place


Getting started
===============
`slidedeck` can be installed with `pip`.

```
$ pip install slidedeck
```

Create a new project, complete with some template slides, the css, and the javascript.
```
$ slidedeck create my_slides
```

Look in there for the `slides.md` file, and edit it to your liking. When you want to see
your work, compile the slides from markdown into HTML.
```
$ slidedeck render
```

You can also have the HTML *auto-compiled* from markdown, any time the files change on disk.
```
$ slidedeck watch
```

If you're curious about how any of these commands work, pass the `-h` flag to the command
line executable,

```
$ slidedeck -h
$ slidedeck create -h
```

Tricks
======

`slidedeck watch` works nicely with the [tincr](http://tin.cr/) extension for
chrome, which will refresh your browser every time the html files its serving
are changed on disk.  

### Adding molecules with JSmol
If you have internet access, you can add a molecule to your slides by using 
```html
<script type="text/javascript" src="http://chemapps.stolaf.edu/jmol/jmol.php?pdbid=1A9U&inline&script=cartoon only"></script>
```
more options are explained [here](http://chemapps.stolaf.edu/jmol/jmol.php).

For an offline version, you need a local copy of JSmol.min.js, and j2s (see the [JSmol wiki](http://wiki.jmol.org/index.php/Jmol_JavaScript_Object#Installation)). 

Then add the following to the header of base.html
```html
<script type="text/javascript" src="JSmol.min.js"></script>
<script type="text/javascript">
    var Info = {
        height: 500,
        width: 500,
        use: "HTML5"
    };
</script>
```
And insert
```html
<script type="text/javascript">
  jmolApplet0 = Jmol.getApplet("jmolApplet0", Info);
  Jmol.script(jmolApplet0,"background white; load 1A9U.pdb; cartoon only;")
</script>
```
in the slide where you want the molecule to appear.

Examples
========

Below are some examples of slides using this deck.  

https://rawgit.com/kyleabeauchamp/BPS2015/master/index.html

https://rawgit.com/kyleabeauchamp/DefenseSlides/master/index.html

http://rawgit.com/kyleabeauchamp/MSMBuilderTalk/master/index.html

License
-------
```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
```

