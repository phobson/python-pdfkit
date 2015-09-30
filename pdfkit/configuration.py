# -*- coding: utf-8 -*-
import subprocess
import sys
from pkg_resources import resource_filename


class Configuration(object):
    def __init__(self, wkhtmltopdf=None, meta_tag_prefix='pdfkit-'):
        self.meta_tag_prefix = meta_tag_prefix
        if wkhtmltopdf is None:
            wkhtmltopdf = resource_filename('pdfkit', 'wkhtmltopdf.exe')
        self.wkhtmltopdf = wkhtmltopdf

        if not self.wkhtmltopdf:
            if sys.platform == 'win32':
                self.wkhtmltopdf = subprocess.Popen(
                    ['where', 'wkhtmltopdf'], stdout=subprocess.PIPE).communicate()[0].strip()
            else:
                self.wkhtmltopdf = subprocess.Popen(
                    ['which', 'wkhtmltopdf'], stdout=subprocess.PIPE).communicate()[0].strip()

        try:
            with open(self.wkhtmltopdf) as f:
                pass
        except IOError:
            raise IOError('No wkhtmltopdf executable found: "%s"\n'
                          'If this file exists please check that this process can '
                          'read it. Otherwise please install wkhtmltopdf - '
                          'https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf' % self.wkhtmltopdf)
