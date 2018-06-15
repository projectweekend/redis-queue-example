from time import sleep

from redis import Redis
from rq import Queue


redis_conn = Redis(host='redis', port=6379)
q = Queue('hello_echo', connection=redis_conn)


def main():
    sleep(5)
    names = ['bob', 'alice', 'frank']
    jobs = []

    for name in names:
        jobs.append(q.enqueue('tasks.hello_echo', name))

    for job in jobs:
        while job.result is None:
            sleep(0.1)
        print(job.result)


if __name__ == '__main__':
    main()
