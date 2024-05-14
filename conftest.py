from pytest import fixture

from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import medusa, megomi, ligoba, limona, sopuki, tomute, linaki


list_of_examples = []
for i in range(256):
    list_of_examples.append(
        Boolf(i, arity=3)
    )


list_of_examples += [
    medusa, megomi, ligoba, limona, sopuki, tomute, linaki
]


@fixture(params=list_of_examples)
def boolf_examples(request):
    yield request.param
