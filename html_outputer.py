# -*- coding: utf-8 -*-

import sys

class HtmlOutputer(object):
    """docstring for HtmlOutputer"""

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')
        type = sys.getfilesystemencoding()

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<tabel>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode(type))
            fout.write('<td>%s</td>' % data['summary'].encode(type))
            fout.write('</tr>')

        fout.write('</tabel>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
