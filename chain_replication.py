import time
import itertools

from multiprocessing import current_process
from distsim import Network, Node, Link, Message

from collections import namedtuple


RequestMsg = namedtuple("RequestMsg", ["operation", "key", "value"])
ChainMsg = namedtuple("ChainMsg", ["head", "tail", "predecessor", "successor"])


def master_code():
    node: Node = current_process()

    logger = node.init_logger()


def client_code():
    node: Node = current_process()

    logger = node.init_logger()


def node_code():
    node: Node = current_process()

    logger = node.init_logger()


if __name__ == "__main__":
    max_number_of_chain = 4

    master = Node("master", master_code)
    client = Node("client", client_code)
    chain = [Node(f"chain_{idx}", node_code) for idx in range(max_number_of_chain)]

    nodes = chain + [master] + [client]
    links = [Link(n1.name, n2.name) for n1, n2 in itertools.combinations(nodes, 2)]

    network = Network(nodes, links)

    network.start()
    time.sleep(5)
    network.kill()
