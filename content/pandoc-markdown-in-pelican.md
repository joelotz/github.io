---
Title: Use Pandoc Markdown in Pelican
Date: 2021-01-31
Tags: Pandoc, Pelican
Keywords: pandoc-reader, pandoc on pelican, converting markdown with pelican
Version: Pelican, 4.5.4, Pandoc, 2.11, Pandoc-Reader, 1.0.0, Python, 3.7.9
---


This article documents installing the pelican plugin [Pandoc-Reader](https://pypi.org/project/pelican-pandoc-reader/), which changes the engine that converts [Markdown](https://www.markdownguide.org/basic-syntax/) syntax to html from the standard [Python-Markdown](https://python-markdown.github.io/) to [Pandoc. ](https://pandoc.org/). 

**Why?** Pandoc is awesome on many levels, but specifically for this blog, it allows me to write pandoc's flavor of markdown. I added [Python-Markdown Extensions](https://python-markdown.github.io/extensions/) which gave some cool features, but it still didn't satisfy me. 

Some of my personal favorite features are:

- Figure Captions!
- Footnotes
- Emojis
- Internal Links

One feature it doesn't have are reStructured-like [admonitions](https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/Admonitions.html). This is something that Markdown Extensions had  :disappointed: - but I saw a Pandoc filter that looked like it will implement those.

### Installation

The installation is easy and the instructions are clear. Make sure you have at least Pandoc 2.11, then pip install the plugin.

```bash
python -m pip install pelican-pandoc-reader
```

One note is that your metadata (Title:, Date:, etc.) has to be in YAML format. That is means fenced by triple dashes. Example:
```plaintext
---
Title: Me
Date: 2021-01-01
---
```

If you already have a bunch of articles written, [here](https://gist.github.com/joelotz/fc92891d13c71021cf4359e492ab3f8c) is a simple python script that should convert it for you. 

You also need to add these variables to the `pelicanconf.py` file. 

```python
# Arguments passed into pandoc
PANDOC_ARGS = [
    "--mathjax",
]

# Non-Pandoc Extensions that are not enabled by default in pandoc
# 	https://pandoc.org/MANUAL.html#non-pandoc-extensions
PANDOC_EXTENSIONS = [
    "+abbreviations",
    "+backtick_code_blocks",
    "+emoji"
    ]
```

## Pandoc Markdown
Here are some examples of the cool features built-in Pandoc Markdown.

### Figure Captions 

![This is my figure caption.](/images/2021/cute-dog.jpg)

Note
~ I've applied styling to the figure and figure captions within my CSS Stylesheets.
 
### Footnotes
MARKDOWN:
```plaintext
Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.
```
HTML RESULT:

Here is a footnote reference,[^1] and another.[^longnote]

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

### Emojis

Pandoc converys textual emojis into Unicode emoticons.
<https://www.webfx.com/tools/emoji-cheat-sheet/>

MARKDOWN:
```plaintext
 :smiley:
 :cow:
```
 
 HTML RESULT:

 - :smiley:
 - :cow:

### Links
MARKDOWN:
```plaintext
You can go directly to <https://.google.com> to find it.
```
HTML RESULT:

You can go directly to <https://google.com> to find it.

MARKDOWN:
```plaintext
Go see the very last header named [MathJax](#mathjax)
```
HTML RESULT:

Go see the very first header named [SmartyPants](#smartypants)


### SmartyPants

Write this in MARKDOWN:
```plaintext
"curly quotes"
... are ellipses
-- are en-dashes
--- are em-dashes
```

To get this HTML RESULT:

- "curly quotes"
- ... are ellipses
- -- are en-dashes
- --- are em-dashes

### Line Blocks

MARKDOWN:
```plaintext
| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

| 200 Main St.
| Berkeley, CA 94718
```

HTML RESULT:  

| The limerick packs laughs anatomical
| In space that is quite economical.
|    But the good ones I've seen
|    So seldom are clean
| And the clean ones so seldom are comical

| 200 Main St.
| Berkeley, CA 94718

### Lists
MARKDOWN:
```plaintext
COMPACT LISTS
-------------
* one
* two
* three
```
HTML RESULT:

* one
* two
* three
```plaintext
LOOSE LISTS
-----------
* one

* two

* three
```
HTML RESULT: 

* one

* two

* three

### Fancy List
MARKDOWN:
```plaintext
(1) One
(2) Two
	a. 2.1
	b. 2.2
(3) Three
```
HTML RESULT: 

(1) One
(2) Two
	a. 2.1
	b. 2.2
(3) Three

MARKDOWN:
```plaintext
#. one
#. two
#. three
```
HTML RESULT: 

#. one
#. two
#. three

### StartNum
MARKDOWN:
```plaintext
 9)  Ninth
10)  Tenth
11)  Eleventh
       i. subone
      ii. subtwo
     iii. subthree
```
HTML RESULT: 

 9)  Ninth
10)  Tenth
11)  Eleventh
       i. subone
      ii. subtwo
     iii. subthree

### Defintion Lists
MARKDOWN:
```plaintext
Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b
```
HTML RESULT: 

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b

\*\*NOTE: I styled the definitions with CSS

### Example Lists
MARKDOWN:
```plaintext
(@)  My first example will be numbered (1).
(@)  My second example will be numbered (2).

Explanation of examples.

(@)  My third example will be numbered (3).
```
HTML RESULT: 

(@)  My first example will be numbered (1).
(@)  My second example will be numbered (2).

Explanation of examples.

(@)  My third example will be numbered (3).

### Superscript and Subscripts
MARKDOWN:
```plaintext
H~2~O is a liquid.  2^10^ is 1024.
```
HTML RESULT: 

H~2~O is a liquid.  2^10^ is 1024.

### Strikeout
MARKDOWN:
```plaintext
This ~~is deleted text.
```
HTML RESULT: 

This ~~is deleted text.~~

### Small Caps
MARKDOWN:
```plaintext
[Hello Everyone]{.smallcaps}, how are you doing?
```
HTML RESULT:

[Hello Everyone]{.smallcaps}, how are you doing?


### MathJax
MARKDOWN:
```plaintext
This is an inline math $y = mx +b$ which is cool.
```
HTML RESULT:

This is an inline math $y = mx +b$ which is cool.

MARKDOWN:
```plaintext
This is a full math equation.
$$ y = mx +b $$ 
```
HTML RESULT:

This is a full math equation.
$$ y = mx +b $$ 

<!--
### Admonitions
 BREAK 

::::: {.admonition .error}

:::::::: {.admonition-title}
Error 
::::::::
This is the message
:::::

::::: {.admonition .error}

[Error]{.admonition-title}
This is the message
:::::
-->