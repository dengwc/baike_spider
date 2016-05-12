# -*- coding: utf-8 -*-

import sys

class HtmlOutputer(object):
    """docstring for HtmlOutputer"""

    def __init__(self):
        self.datas = []
        self.data_dir = './data/'

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        type = sys.getfilesystemencoding()

        for data in self.datas:
            output_file = self.data_dir + data['title']
            fout = open(output_file, 'w+')
            fout.write(data['summary'].encode(type))

        fout.close()
