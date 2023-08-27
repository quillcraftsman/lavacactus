# Internationalization

## Using internationalization with LavaCactus

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
