#!/usr/bin/env python
import os.path
from pstats import Stats
import json
from urllib.parse import quote
import tornado.ioloop
import tornado.web
from .stats import table_rows, json_stats

settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'debug': True,
    'gzip': True
}

class VizHandler(tornado.web.RequestHandler):
    def get(self, profile_name):
        abspath = os.path.normpath(os.path.join('/', profile_name))
        if os.path.isdir(abspath):
            self._list_dir(abspath)
        else:
            try:
                s = Stats(abspath)
            except Exception:
                raise RuntimeError('Could not read %s.' % abspath)
            self.render(
                'viz.html', profile_name=profile_name,
                table_rows=table_rows(s), callees=json_stats(s))

    def _list_dir(self, abspath):
        entries = os.listdir(abspath)
        parent = os.path.normpath(os.path.join(abspath, '..'))
        dir_entries = [[[
            '..',
            '/snakeviz' + parent
        ]]]
        for name in sorted(entries):
            if name.startswith('.'):
                continue
            fullname = os.path.join(abspath, name)
            displayname = name
            if os.path.isdir(fullname):
                displayname += '/'
            if os.path.islink(fullname):
                displayname += '@'
            dir_entries.append(
                [[displayname, '/snakeviz' + fullname]])
        self.render(
            'dir.html', dir_name=abspath, dir_entries=json.dumps(dir_entries))

handlers = [(r'/snakeviz/(.*)', VizHandler)]
app = tornado.web.Application(handlers, **settings)

if __name__ == '__main__':
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
