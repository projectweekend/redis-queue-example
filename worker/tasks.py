from rq.decorators import job


@job('hello_echo', timeout=3)
def hello_echo(message):
    return 'hello {0}'.format(message)
