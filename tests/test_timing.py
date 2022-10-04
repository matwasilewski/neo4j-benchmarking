import pytest
from neo4j_benchmarking.utils.timing import timeit 


@timeit
def sample_func():
    return "sample_output_str"

def test_timeit():
    time_taken, output = sample_func()
    assert output == "sample_output_str"
    assert type(time_taken) == float
