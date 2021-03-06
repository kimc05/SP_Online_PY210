#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'
    indent = "    "
    def __init__(self, content=None, **kwargs):
        if content is None:
            self.contents = []
        else:
            self.contents = [content]
        self.attributes = kwargs

    def append(self, new_content):
        self.contents.append(new_content)

    def _open_tag(self, cur_ind = ''):
        open_tag = ["{}<{}".format(cur_ind, self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        open_tag = "".join(open_tag)
        return open_tag

    def _close_tag(self, cur_ind = ''):
        close_tag = "{}</{}>\n".format(cur_ind, self.tag)
        return close_tag

    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(self.indent + cur_ind + content)
            out_file.write('\n')
        out_file.write(self._close_tag(cur_ind))


class Html(Element):
    tag = 'html'
    def render(self, out_file, cur_ind=''):
        out_file.write("{}<!DOCTYPE html>\n".format(cur_ind))
        super().render(out_file, cur_ind)


class Body(Element):
    tag = 'body'


class Head(Element):
    tag = 'head'


class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'


class OneLineTag(Element):
    tag = 'OneLineTag'


    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class Title(OneLineTag):
    tag = "title"


# step 4 tests
class P(Element):
    tag = 'p'


class OneLineTag(Element):

    def render(self, out_file, cur_ind=''):
        out_file.write(self._open_tag(cur_ind))
        out_file.write(self.contents[0])
        out_file.write(self._close_tag())
    def append(self, content):
        raise NotImplementedError

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Title(OneLineTag):
    tag = 'title'

class H(OneLineTag):

    def __init__(self, size, content=None, **kwargs):
        self.tag = "h{}".format(size)
        super().__init__(content, **kwargs)

class SelfClosingTag(Element):

    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag should not content")
        super().__init__(content=content, **kwargs)


    def render(self, out_file, cur_ind=''):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(cur_ind)
        out_file.write(tag)


    def append(self, *args):
        raise TypeError("append error, no content can be added to a SelfClosingTag")
class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class Meta(SelfClosingTag):
    tag = 'meta'
