import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Served successfully.")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])
    port = 8888
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
