# Werkzeug is a WSGI (web service gateway interface) and 
# it allows servers and Python applications to communicate much more easily

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5556,
        application=application
    )
