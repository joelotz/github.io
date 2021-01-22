Title: Adding Python-Markdown Extensions in Pelican 
Date: 2021-01-21
Tags: Pelican, Markdown
Keywords: python-markdown, pelican, markdown, definition list, admonitions
Version: Pelican, 4.5.4, Python-Markdown, 3.3.3



### Definition List
This first extension I implemented are definitions. They were not critical but thought would be interesting. Here is the markdown syntax to implement within your post.
```reStructuredText
Apple 
:  Pomaceous fruit of plants of the genus Malus in the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.
```
Once Python-Markdown does it's thing, it shoudl render out html that looks like this.
```html
<dl>
<dt>Apple</dt>
<dd>Pomaceous fruit of plants of the genus Malus in the family Rosaceae.</dd>
<dt>Orange</dt>
<dd>The fruit of an evergreen tree of the genus Citrus.</dd>
</dl>
```
At which point you style it however you want. This is how I styled mine.
```css
dl {
  border: 3px double #ccc;
  padding: 0.5em;
}

dt {
  float: left;
  clear: left;
  width: 100px;
  text-align: right;
  font-weight: bold;
}

dt::after {
  content: ":";
}

dd {
  margin: 0 0 0 110px;
  padding: 0 0 0.5em 0;
}
```
And finally, here is what it looks like rendered out.

Apple 
:  Pomaceous fruit of plants of the genus Malus in the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.

I'm not sold on the border, but it's still a good example. 

### Admonition

One really cool built-in feature of reStructuredText are directives called [Admonitions](https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/Admonitions.html). These are like pop-ups that you see in [Sphinx](https://www.sphinx-doc.org/en/master/) documentation.

[Pelican](https://docs.getpelican.com/en/latest/) uses [Python-Markdown](https://python-markdown.github.io/) for it's markdown parsing and Python-Markdown has these [extensions](https://python-markdown.github.io/extensions/) that include [admonitions](https://python-markdown.github.io/extensions/admonition/). All these extensions can be activated by adding the `MARKDOWN` variable to your `pelicanconf.py` configuration file as defined in the [pelican setting docs](https://docs.getpelican.com/en/latest/settings.html?highlight=MARKDOWN#basic-settings):

The reStructuredText documents says:

> The following admonition directives have been implemented:
> - attention
> - caution
> - danger
> - error
> - hint
> - important
> - note
> - tip
> - warning

Withing your pelican blog, type the following code in Markdown syntax

```reStructuredText
!!! note
	Here is a note you should know.
```

And the Python-Markdown parser turns the Markdown into the following HTML
```html
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Here is a note you should know.</p>
</div>
```
Once you have the HTML output you can style them hoever you want with CSS. Here is my [CSS stylesheet](https://gist.github.com/joelotz/ab3ca713bc353d6f31e8a8fae186a705) that styles the following.

!!! note
	Here is a note you should know.

Here are some more examples of different admonitions.

```reStructuredText
!!! important
	Pay attention, very important!
```
!!! important
	Pay attention, very important!

```reStructuredText
!!! warning
	This is a warning
```
!!! warning
	This is a warning with some inline `code`

```reStructuredText
!!! attention
	Pay attention, very important!
```
!!! attention
	Pay attention, very important!

```reStructuredText
!!! caution
	Be careful here.
```
!!! caution
	Watchout! 

```reStructuredText
!!! danger
	This is really dangerous!
```

Follow the pattern and you can make the more like this.

!!! danger
	This is really dangerous!

!!! error
	You done messed up now

!!! tip
	Don't spit into the wind.
	
!!! hint
	This is a hint

### SmartyPants
Finally, here is the implementation of [SmartyPants](https://daringfireball.net/projects/smartypants/) which intelligently turns ASCII typography into "pretty" HTML entities.

| Markdown Syntax | Rendered HTML |
|-----------------|---------------|
|`'test'` | 'test'|
|`"test"` | "test"|
|`<<test>>` | << test >> ([guillemets](https://en.wikipedia.org/wiki/Guillemet)) |
|`...` | ...  ([ellipse](https://en.wikipedia.org/wiki/Ellipsis)) |
|`--` | -- ([en dash](https://en.wikipedia.org/wiki/Dash#En_dash)) |
|`---` | --- ([em dash](https://en.wikipedia.org/wiki/Dash#Em_dash)) |

### Configuration File

To "activate" these extensions you have to set the variable in your `peliconconf.py` file. Here are the settings I used.

```
:::python
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'},
    },
    'output_format': 'html5',
}
```