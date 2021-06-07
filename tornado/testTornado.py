from abc import ABC
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3


class IndexHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        query = 'create table if not exists task (id integer primary key, name text, status numeric)'
        _execute(query)
        query = 'select * from task'
        todos = _execute(query)
        self.render('index.html', todos=todos)


class NewHandler(tornado.web.RequestHandler, ABC):
    def post(self):
        name = self.get_argument('name', None)
        query = "insert into task (name, status) values ('%s', 1)" % name
        _execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')


class UpdateHandler(tornado.web.RequestHandler, ABC):
    def get(self, id_, status):
        query = f'update task set status={int(status)} where id={id_}'
        _execute(query)
        self.redirect('/')


class DeleteHandler(tornado.web.RequestHandler, ABC):
    def get(self, id_):
        query = f'delete from task where id={id_}'
        _execute(query)
        self.redirect('/')


class RunApp(tornado.web.Application):
    def __init__(self):
        handlers = [('/', IndexHandler),
                    ('/todo/new', NewHandler),
                    (r'/todo/update/(\d+)/status/(\d+)', UpdateHandler),
                    (r'/todo/delete/(\d+)', DeleteHandler)]
        settings = dict(debug=True, template_path='templates', static_path='static')
        super().__init__(handlers, **settings)


def _execute(query):
    db = sqlite3.connect('testTornado')
    cursor = db.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    return res


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(8000)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except Exception:
        print('Stop http server 8000')
        http_server.stop()
