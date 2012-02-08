# coding: utf-8
import jinja2
from dext.forms import forms, fields


class ForumField(fields.TextField):

    @property
    def command_line(self):
        return u'''
<div class="pgf-command-line command-line">
<a class="pgf-command" href="#" data-tag="b" data-tooltip="[b]<strong>жирный</strong>[/b]">[b]</a>
<a class="pgf-command" href="#" data-tag="i" data-tooltip="[i]<i>курсив</i>[/i]">[i]</a>
<a class="pgf-command" href="#" data-tag="u" data-tooltip="[u]<u>подчёрнутый</u>[/u]">[u]</a>
<a class="pgf-command" href="#" data-tag="s" data-tooltip="[s]<strike>зачёркнутый</strike>[/s]">[s]</a>
<a class="pgf-command" href="#" data-tag="img" data-tooltip="[img]http://адрес картинки[/img]">[img]</a>
<a class="pgf-command" href="#" data-tag="url" data-tooltip='[url="http://адрес"]текст[/url]'>[url]</a>
</div>
'''

    def html(self, bound_field):
        return jinja2.Markup(bound_field.label_tag()) + jinja2.Markup(self.command_line) + jinja2.Markup(bound_field) + bound_field.errors_container
    

class NewPostForm(forms.Form):

    text = ForumField(label=u'Текст')


class NewThreadForm(NewPostForm):

    caption = fields.CharField(label=u'Название', max_length=256)
