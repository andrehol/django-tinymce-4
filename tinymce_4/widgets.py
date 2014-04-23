# -*- coding: utf-8 -*-
import json
from django import forms
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from tinymce_4 import settings as tinymce_settings


class TinyMCEWidget(forms.Textarea):
    """
    Textarea form widget with support TinyMCE.
    See: http://www.tinymce.com/wiki.php/TinyMCE
    """

    _css_class = 'tinymce'

    def __init__(self, attrs=None):
        attrs = attrs or {}
        css_class = attrs.get('class', '')
        attrs['class'] = ' '.join([css_class, self._css_class])
        super(TinyMCEWidget, self).__init__(attrs)

    class Media:
        css = {
            'all': ('tinymce_4/tinymce/tinymce.css',)
        }

        js = [
            'tinymce_4/tinymce/tinymce.min.js',
            'tinymce_4/tinymce/setup/django-filebrowser.js',
        ]



class TinyMCEFullWidget(TinyMCEWidget):
    """
    Textarea form widget with support TinyMCE.
    See: http://www.tinymce.com/wiki.php/TinyMCE
    This is widget for full config TinyMCE.
    """

    # def render(self, name, value, attrs=None):
    #     if value is None: value = ''
    #     final_attrs = self.build_attrs(attrs, name=name)
    #     mce_json = json.dumps(tinymce_settings.DEFAULT_CONFIG.copy())
    #     html = '<textarea%s>\r\n%s</textarea>' % (forms.widgets.flatatt(final_attrs),
    #                                               force_text(value))
    #     html += '<script type="text/javascript">tinymce.init(%s)</script>' % mce_json
    #     print
    #     print html
    #     print
    #     return mark_safe(html)

    class Media:
        js = [
            'tinymce_4/tinymce/setup/full.js',
        ]


class TinyMCESmallWidget(TinyMCEWidget):
    """
    Textarea form widget with support TinyMCE.
    See: http://www.tinymce.com/wiki.php/TinyMCE
    This is widget for small config TinyMCE.
    """

    class Media:
        js = [
            'tinymce_4/tinymce/setup/small.js',
        ]
