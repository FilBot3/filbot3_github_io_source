# TexLive and LaTeX

## Overview

Pronounced La-Tech, LaTeX is a typesetting application for making professional documents and formatting them by using code rather than a WYSIWYG Editor like LibreOffice or OpenOffice. There are a few different LaTeX or TeX distributions out there, but I'm going to cover just TexLive and not bash any other ones or really cover them.

Don't let the look of LaTeX scare you, its fantastic once you get it down.

## Requirements

* TexLive Installer
* An operating system (Linux is used here, Windows or MacOS work too)
* A text editor. I prefer Vim, but there are plenty of others.
* A PDF Reader

## Setup

We're going to cover just TexLive, not the other bits. Download the corresponding package from the Tex User Group, TUG, FTP Site.

* [TUG TexLive FTP](ftp://tug.org/historic/systems/texlive/2019/)

The `.tar.gz` is generally for Linux, and `.zip` is generally for Windows. I want to say that either could install, but I'd stick with that unless you're feeling venturous. Run the installer scripts that come with the package. Once this is finished you're ready to perform most LaTeX tasks. MacOS users should use [HomeBrew](https://brew.sh/) to install TexLive for their MacOS systems. It just works better.

## Usage

Open up a Terminal. Windows can use `cmd.exe` but I always use `cmder.exe`, which is a Terminator-like terminal emulator for Windows. It also picks up any other shells that might be in your `%PATH%`, so that's spiffy. Linux use whatever shell you've got, and MacOS, I recommend using iTerm2. Now you can execute a tex command to see if its working.

```bash
texhelp pdflatex
```

The above command spits out the help document for the `pdflatex` command. Spiffy eh? Now you can run any LaTeX commands that come with it. Use `tlshell` to install more packages if needed from CTAN.

## Installing Custom packages with TexLive.

### Packages and Environments.

Generally, you put the expanded, or cloned package into your `${TEXMFHOME}/tex/latex/` directory so its similar to this:

* `${TEXMFHOME}/tex/latex/custom_package/custom.sty`

Then rescan your packages.

### Custom Fonts, mainly OpenType `.otf`

Now if you have any custom fonts, the way I had this working was to place those fonts in a folder under the following directories:

* `${TEXMFDIST}/fonts/opentype/custom_fonts/custom_font_package/`

Inside that directory stucture has the font packages, and in this case, the OpenType Fonts usually ending in `.otf`. Run `mktexlsr` for TexLive to recognize your new fonts. I had to then use `xelatex` or `lualatex`. Something about how those compilers work and how they read packages. If you're not doing anything funky with fonts or `.otf` files, then the plain `pdflatex` should suite you just fine.

## Using `kpsewhich`

Something that helps me when trying to script or figure out where certain
variables are for LaTeX is to use the `kpsewhich` program provided with TexLive.
You can use this like

* `kpsewhich -var-value=TEXMFHOME`

to find out where TexLive is looking for certain variables. Using the TexLive
docs to find out where those are are not fairly obvious to me, so I linke them
here: [TexLive Predefined texmf trees](https://www.tug.org/texlive/doc/texlive-en/texlive-en.html#x1-110002.3). There you'll see a bunch of them. The ones listed
in prior parts of this page, will also work here.

## Bonus

If you're feeling froggy, you can use something like Ruby's Guard Gem and have it watch your TeX source files and recompile when you save your work.

## References

* [TUG TexLive Users Guide](https://www.tug.org/texlive/doc/texlive-en/texlive-en.html)
* [Overleaf: Learn LaTeX](https://www.overleaf.com/learn/latex/Main_Page)
* [WikiBooks: LaTeX](https://en.wikibooks.org/wiki/LaTeX)
* [Luke Smith Wanna learn LaTeX?](https://lukesmith.xyz/latex.html)
* [YouTube: LaTeX Playlist](https://www.youtube.com/playlist?list=PL-p5XmQHB_JSQvW8_mhBdcwEyxdVX0c1T)
