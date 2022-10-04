from neo4j import GraphDatabase
import time
from functools import wraps
import time
import click
import json
import datetime


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(
            f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    @timeit
    def match_nodes(self, n):
        with self.driver.session() as session:
            result = session.execute_write(self._match_n_nodes, n)
            print(result)

    @staticmethod
    def _match_n_nodes(tx, n):
        result = tx.run(f"MATCH (n) RETURN n LIMIT {n}")
        return result


@click.command()
@click.option('--limit', default=1, help='limit for number of nodes')
@click.option('--to-file', '-f', is_flag=True, default=False,
              help="Save to a file")
@click.option('--output', '-o', is_flag=True, default=False,
              help="Print output")
def match_nodes(limit, to_file, output):
    connection = Neo4jConnection("bolt://localhost:7688", "neo4j", "biorelate")
    result = connection.match_nodes(limit)
    print(result.data())

    if to_file:
        ts = time.time()
        timestamp_string = datetime.datetime.fromtimestamp(ts).strftime(
            '%Y-%m-%d_%H:%M:%S')

        with open(f"outputs/{timestamp_string}", "w") as f:
            json.dump(f, result.data())

    if output:
        print(result.data())
    connection.close()


if __name__ == "__main__":
    match_nodes()
