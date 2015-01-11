#!/usr/bin/env python
import os

def application(environ, start_response):

    ctype = 'text/plain'
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        ctype = 'text/html'
        response_body = '''1x1=1&nbsp&nbsp1x2=2&nbsp&nbsp1x3=3&nbsp&nbsp1x4=4&nbsp&nbsp1x5=5&nbsp&nbsp1x6=6&nbsp&nbsp1x7=7&nbsp&nbsp1x8=8&nbsp&nbsp1x9=9&nbsp&nbsp<br />2x1=2&nbsp&nbsp2x2=4&nbsp&nbsp2x3=6&nbsp&nbsp2x4=8&nbsp&nbsp2x5=10&nbsp&nbsp2x6=12&nbsp&nbsp2x7=14&nbsp&nbsp2x8=16&nbsp&nbsp2x9=18&nbsp&nbsp<br />3x1=3&nbsp&nbsp3x2=6&nbsp&nbsp3x3=9&nbsp&nbsp3x4=12&nbsp&nbsp3x5=15&nbsp&nbsp3x6=18&nbsp&nbsp3x7=21&nbsp&nbsp3x8=24&nbsp&nbsp3x9=27&nbsp&nbsp<br />4x1=4&nbsp&nbsp4x2=8&nbsp&nbsp4x3=12&nbsp&nbsp4x4=16&nbsp&nbsp4x5=20&nbsp&nbsp4x6=24&nbsp&nbsp4x7=28&nbsp&nbsp4x8=32&nbsp&nbsp4x9=36&nbsp&nbsp<br />5x1=5&nbsp&nbsp5x2=10&nbsp&nbsp5x3=15&nbsp&nbsp5x4=20&nbsp&nbsp5x5=25&nbsp&nbsp5x6=30&nbsp&nbsp5x7=35&nbsp&nbsp5x8=40&nbsp&nbsp5x9=45&nbsp&nbsp<br />6x1=6&nbsp&nbsp6x2=12&nbsp&nbsp6x3=18&nbsp&nbsp6x4=24&nbsp&nbsp6x5=30&nbsp&nbsp6x6=36&nbsp&nbsp6x7=42&nbsp&nbsp6x8=48&nbsp&nbsp6x9=54&nbsp&nbsp<br />7x1=7&nbsp&nbsp7x2=14&nbsp&nbsp7x3=21&nbsp&nbsp7x4=28&nbsp&nbsp7x5=35&nbsp&nbsp7x6=42&nbsp&nbsp7x7=49&nbsp&nbsp7x8=56&nbsp&nbsp7x9=63&nbsp&nbsp<br />8x1=8&nbsp&nbsp8x2=16&nbsp&nbsp8x3=24&nbsp&nbsp8x4=32&nbsp&nbsp8x5=40&nbsp&nbsp8x6=48&nbsp&nbsp8x7=56&nbsp&nbsp8x8=64&nbsp&nbsp8x9=72&nbsp&nbsp<br />9x1=9&nbsp&nbsp9x2=18&nbsp&nbsp9x3=27&nbsp&nbsp9x4=36&nbsp&nbsp9x5=45&nbsp&nbsp9x6=54&nbsp&nbsp9x7=63&nbsp&nbsp9x8=72&nbsp&nbsp9x9=81&nbsp&nbsp<br />'''

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body.encode('utf-8') ]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
