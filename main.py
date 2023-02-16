import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues

from primes import is_prime, NUMBERS


class PrimeResult(NamedTuple):
    n: int
    prime: bool
    elapsed: float


JobQueue = queues.SimpleQueue[int]
ResultQueue = queues.SimpleQueue[PrimeResult]


def check(n: int) -> PrimeResult:
    t0 = perf_counter()
    res = is_prime(n)
    return PrimeResult(n, res, perf_counter() - t0)


def worker(jobs: JobQueue, results: ResultQueue) -> None:
    while n := jobs.get():
        results.put(check(n))
    results.put(PrimeResult(0, False, 0.0))


def start_jobs(
        procs: int, jobs: JobQueue, results: ResultQueue
) -> None:
    for n in NUMBERS:
        jobs.put(n)

    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put()
