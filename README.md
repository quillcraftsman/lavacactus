# LavaCactus

<hr>

#### Workflows
[![Tests](https://github.com/quillcraftsman/lavacactus/actions/workflows/testing.yml/badge.svg?branch=master)](https://github.com/quillcraftsman/lavacactus/actions/workflows/testing.yml)

[//]: # ([![Pylint]&#40;https://github.com/quillcraftsman/lavacactus/actions/workflows/lint.yml/badge.svg?branch=main&#41;]&#40;https://github.com/quillcraftsman/lavacactus/actions/workflows/lint.yml&#41;)

#### Package
[![Version](https://img.shields.io/pypi/v/lava-cactus.svg)](https://pypi.python.org/pypi/lava-cactus/)
[![Development Status](https://img.shields.io/pypi/status/lava-cactus.svg)](https://pypi.python.org/pypi/lava-cactus)
[![Python version](https://img.shields.io/pypi/pyversions/lava-cactus.svg)](https://pypi.python.org/pypi/lava-cactus/)
[![License](https://img.shields.io/pypi/l/lava-cactus)](https://github.com/quillcraftsman/lava-cactus/blob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/lava-cactus.svg)](https://pypi.python.org/pypi/lava-cactus/)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/quillcraftsman/lavacactus/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/quillcraftsman/lavacactus/issues/)

#### Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/lava-cactus)](https://pepy.tech/project/lava-cactus)
[![Week Downloads](https://img.shields.io/pypi/dw/lava-cactus)](https://pepy.tech/project/lava-cactus)
[![Month Downloads](https://img.shields.io/pypi/dm/lava-cactus)](https://pepy.tech/project/lava-cactus)
[![All Downloads](https://img.shields.io/pepy/dt/lava-cactus)](https://pepy.tech/project/lava-cactus)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/quillcraftsman/lavacactus)](https://github.com/quillcraftsman/lavacactus/)
[![Top Language](https://img.shields.io/github/languages/top/quillcraftsman/lavacactus)](https://github.com/quillcraftsman/lavacactus/)

#### Development
- [![Release date](https://img.shields.io/github/release-date/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus/releases)
[![Last Commit](https://img.shields.io/github/last-commit/quillcraftsman/lavacactus/master
)](https://github.com/quillcraftsman/lavacactus/)
- [![Issues](https://img.shields.io/github/issues/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus/issues/)
- [![Pull Requests](https://img.shields.io/github/issues-pr/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus/pulls)
- [![Discussions](https://img.shields.io/github/discussions/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus/discussions/)

#### Repository Stats
[![Stars](https://img.shields.io/github/stars/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus)
[![Contributors](https://img.shields.io/github/contributors/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/django-dry-tests/graphs/lavacactus)
[![Forks](https://img.shields.io/github/forks/quillcraftsman/lavacactus
)](https://github.com/quillcraftsman/lavacactus)

* [What is LavaCactus](https://github.com/quillcraftsman/lavacactus#what-is-lavacactus)
* [Examples](https://github.com/quillcraftsman/lavacactus#examples)
* [Super quick tutorial](https://github.com/quillcraftsman/lavacactus#super-quick-tutorial)
* [Contribute](https://github.com/quillcraftsman/lavacactus#contribute)
* [Extended guide](https://github.com/quillcraftsman/lavacactus#extended-guide)

## What is LavaCactus

LavaCactus is the static site generator (SSG) based on [Cactus][cactus_github_page] ported to use with **python 3.12 and django 4**

The original library work with Python 2.6, 2.7, 3.4 and 3.5 and django<2.0

Now it works on **python 3.10-3.12**

## What is Cactus

Cactus is a simple but powerful static website generator using Python and the [Django template system][django_templates].
Cactus also makes it easy to develop locally and deploy your site to S3 directly.
It works great for company, portfolio, personal, support websites and blogs.

## What is new in LavaCactus

* LavaCactus work with python 3.12 (3.10-3.12) and Django 5 (>=2.0) 
* LavaCactus can make structure for multilanguage sites
* LavaCactus has GitHub action to publish build on GitHub pages

## Examples

  + https://lavacactus.craftsman.lol - LavaCactus app site and base template example
  + https://craftsman.lol - quill craftsman about website
  + https://libresource.info/ - Libresource GitHub organization website (multi-language example)

## Super quick tutorial

Install LavaCactus from pypi

    pip install lava-cactus

If you saw no errors, you can now generate a new project

    cactus create my-new-project

Where `my-new-project` is the project directory

    cd my-new-project

After that you can change your site with django templates. After that just `build` to create static pages

    cactus build

To start editing and previewing your site type the following. Then point your browser to localhost:8000 and start editing. Cactus will automatically rebuild your project and refresh your browser on changes.

    cactus serve

If you use serve your site will be work on test server and you can use /index.html - links starts with /.
The other way it's to use browser and index.html static file. In this way use index.html in links (without / at the beginning).

## Contribute

You're welcome!

To get started:
* [Developer Guidelines](https://github.com/quillcraftsman/lavacactus/blob/master/CONTRIBUTING.md)
* [Developer Documentation](https://github.com/quillcraftsman/lavacactus/blob/master/DEVELOPER_DOCUMENTATION.md)

## Extended guide

### Creating a new project

You can create a new project by generating a new project structure like this. Make sure the destination folder does not
exist yet.

    cactus create [path]

If you did not see any errors, the path you pointed to should now look like this.

    - .build                Generated site (upload this to your host)
    - .github               CI/CD github action to publish your site on github pages
    - locale                Instruction how to use translations if you need
    - pages                 Your actual site pages
        - about.html
        - contact.html
        - error.html        A default 404 page
        - index.html
        - robots.txt
        - sitemap.xml
    - plugins               A list of plugins. To enable remove disabled from the name
    - static                Directory with static assets
        - css
        - fonts
        - images
        - js
    - templates             Holds your django templates
        - base.html
    - config.json           Configuration file

### Making your site

After generating your site you can start building by adding pages to contents, which can rely on templates. So for
example if you want a page `/articles/2010/my-article.html` you would create the file with directories in your pages
folder. Then you can edit the file and use django's template features.

### Building your site

When you build your site it will generate a static version in the build folder that you can upload to any host.
Basically it will render each page from your pages folder, copy it over to the build folder and add all the static
assets to it so it becomes a self contained website. You can build your site like this:

    cd [your-cactus-path]
    cactus build

Your rendered website can now be found in the (hidden) [path]/.build folder. Cactus can also run a small webserver to
preview your site and update it when you make any changes. This is really handy when developing to get live visual feedback.

You can run it like this:

    cactus serve

### Linking and contexts

Cactus makes it easy to relatively link to pages and static assets inside your project by using the template tags
{% static %} and {% url %}. For example if you are at page `/blog/2011/Jan/my-article.html` and would like to link to
`/contact.html` you would write the following:

    <a href="{% url '/contact.html' %}">Contact</a>

Just use the URL you would normally use: don't forget the leading slash.

### Templates

Cactus uses the Django templates. They should be very similar to other templating systems and have some nice
capabilities like inheritance. In a nutshell: a variable looks like this `{{ name }}` and a tag like this
`{% block title %}Welcome{% endblock %}`. You can read the [full documentation][django_templates] at the django site.

### Enabling Plugins

To enable a plugin for your site, change the file name from [PLUGIN].disabled.py to [PLUGIN].py.

### Internationalization

#### Using internationalization with LavaCactus

To enable internationalization for your project:

  1. Add a `use_translate` key to your configuration file
  2. Add `default_language` key to your configuration file with main language. For example `default_language="en"`
  3. Add `other_languages` key to your configuration file with the list of the other languages. 
     For example `other_languages=["ua", "ru"]`
  4. Mark strings for translation in your site (using `{% trans %}`)
  5. Put `{% load i18n %}` at the top of template with `trans` tags 
  6. Run `cactus messages:make`
  7. Edit the .po file that was created with translations.
  8. Run `cactus build` to create multilanguage site structure

### Extras

Modify `config.json` to set a custom blog path, default author name, or date pattern used to parse metadata. The defaults are:

    "blog": {
        "path": "blog",
        "author": "Unknown",
        "date-format": "%d-%m-%Y"
    }

#### YAML Variables
By default you can declare variables to be included above each page, for example:

```
test_text: Lorem Ipsum

<p>{{ test_text }}</p>
```

You can declare the variables using YAML instead. Just surround the block with the `---`
and `...` [Document Separators](http://yaml.org/spec/1.1/#id857577). Then the objects
and arrays will be available inside the templates:

```
---
header_text: Lorem Ipsum
custom_object:
  name: Lorem
  description: Ipsum
custom_array:
  -
    name: lorem
  -
    name: ipsum
...

{% for item in custom_array %}
  <p>{{ header_text }}: {{ item.name }}</p>
{% endfor %}

<p>{{ custom_object.name }} | {{ custom_object.description }}</p>
```

The *PyYAML* library is used for this functionality.

#### Asset pipeline

Cactus comes with an asset pipeline for your static files. If you'd like to use it, make sure you use the {% static %}
template tag to link to your static assets: they might be renamed in the process.


##### Fingerprinting

Modify `config.json`, and add the extensions you want to be fingerprinting:

    "fingerprint": [
        "js",
        "css"
    ],

This lets you enable caching with long expiration dates. When a file changes, its name will reflect the change. Great for when you use a CDN.


##### Optimization

Modify `config.json`, and add the extensions you want to be optimizing:

    "optimize": [
        "js",
        "css"
    ],


By default, Cactus will use:

  + YUI for CSS minification
  + Closure compiler for JS minification (YUI is built-in too, so you can use it!)

Check out `plugins/static_optimizes.py` in your project to understand how this works. It's very easy to add your own
optimizers!


#### Site URL

If you would like for your sitemap to have absolute paths you need to
add a site-url key to your config.json

You can enable this by adding modifying your configuration and adding:

    "site-url": "http://yoursite.com",

Note that you need to do this if you want your sitemap to be valid for Google Webmaster Tools.


#### "Pretty" URLs

If you would like to not have ".html" in your URLs, Cactus can rewrite those for you, and make "/my-page.html" look
appear as "/my-page/", by creating the "/my-page/index.html" file.

You can enable this by adding modifying your configuration and adding:

    "prettify": true

Note that if you're going to use this, you should definitely set your "Meta canonical" to the URL you're using so as
to not hurt your search rankings:

    <link rel="canonical" href="{{ CURRENT_PAGE.absolute_final_url }}" />

#### Extra files

Cactus will auto generate a `robots.txt` and `sitemap.xml` file for you based on your pages.

This will help bots to index your pages for Google and Bing for example.

[cactus_github_page]: https://github.com/eudicots/Cactus
[django_templates]: http://docs.djangoproject.com/en/dev/topics/templates/
[documentation_path]: https://github.com/quillcraftsman/lavacactus
