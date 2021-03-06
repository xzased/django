from django.test import SimpleTestCase
from django.utils.safestring import mark_safe

from ..utils import render, setup


class LowerTests(SimpleTestCase):

    @setup({'lower01': '{% autoescape off %}{{ a|lower }} {{ b|lower }}{% endautoescape %}'})
    def test_lower01(self):
        output = render('lower01', {"a": "Apple & banana", "b": mark_safe("Apple &amp; banana")})
        self.assertEqual(output, "apple & banana apple &amp; banana")

    @setup({'lower02': '{{ a|lower }} {{ b|lower }}'})
    def test_lower02(self):
        output = render('lower02', {"a": "Apple & banana", "b": mark_safe("Apple &amp; banana")})
        self.assertEqual(output, "apple &amp; banana apple &amp; banana")
