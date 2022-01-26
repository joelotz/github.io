---
Title: Enabling different LaTeX compilers in VS Code
Date: 2022-01-26
Tags: LaTeX
Author: Joe
Keywords: LaTeX, VS Code, LaTeX Workshop, magic comment
Version: Visual Studio Code, 1.63.2, LaTeX Workshop, 8.23.0, Ubuntu, 20.04.3 LTS
---

This post assumes you have already installed both VS Code and the extension [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop). 

To use a different compiler you can either use a magic comment or define a recipe. The extension author warns “it is advised to use the recipe system instead of magic program to define the building process, since the latter is only implemented for backward compatibility.” I'll describe both.

I needed to solve this because the [FortySecondsCV class](https://github.com/PandaScience/FortySecondsCV#Requirements) uses [Academicons](https://jpswalsh.github.io/academicons/) which doesn't work when compiling with pdfLaTeX. So I needed XeLaTeX or LuaLaTeX but wasn't fluent enough in VS Code.

### Magic Comment
First, as of extension version 8.23.0, [magic comments are disabled by default](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile#magic-comments). You must go into your settings file and enable it.

```bash
// This allows magic comments
"latex-workshop.latex.build.forceRecipeUsage": false,
```

After this, defining a different compiler is as simple as placing a comment on the top of your root .tex file place the line:

```bash
%!TEX program = lualatex
```
or
```bash
%!TEX program = pdflatex
```
Other options are program = xelatex, bibtex, etc.

### Recipes
The second method is fairly straightforward and is the recommended method. In your settings file you must define your "tools" and your "recipes" for using tools. This is how you can make complicated workflows like pdflatex -> biber -> pdflatex -> pdflatex (notice also it runs pdflatex twice at the end). 

The tools definition is basically a command and arguments. Here are some examples:

```latex
"latex-workshop.latex.tools": [
    {
    "name": "lualatex",
    "command": "lualatex",
    "args": [
        "-shell-escape", //I can't remember why I needed this in the past 
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-pdf",
        "-output-directory=%OUTDIR%",           
        "%DOC%"
    ],
    "env": {}
    },

    {
    "name": "pdflatex",
    "command": "pdflatex",
    "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-output-directory=%OUTDIR%",
        "%DOC%"
    ],
    "env": {}
    },

    {
    "name": "biber",
    "command": "biber",
    "args": [
	    "%DOCFILE%"
    ],
    "env": {}
    }
],        
```

And then you can define the recipes. The "name" is just a label and the "tools" are what you want to call and what order. Here are some more examples.

```latex
"latex-workshop.latex.recipes": [
    {
        "name": "lualatex",
        "tools": [
            "lualatex"
        ]
    },

    {
        "name": "pdflatex -> biber -> pdflatex TWICE",
        "tools": [
            "pdflatex"
            "biber"
            "pdflatex"
            "pdflatex"
        ]
    }        
],
```

Once you restart VS Code you can find your new recipes under the LaTeX command panel. Note that the first recipe is the default if you simply run "build project."

![](/images/2022/VSCode_Latex.png)
