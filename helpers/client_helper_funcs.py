import time
MAX_INDEX = 289
dict = {}


def get_bname(client: object, index: str):
    '''
    Returns brwose name of a given Node Object without the namespace header

    @Param Node $client
    @Param str $index
    '''
    # print('get_bname')
    node = client.get_node("ns=2;i={}".format(
        index)).get_browse_name().to_string()
    return node[2:]


def update_EPIC_Objects(client: object):
    '''
    Dynamically updates all nodes of the connected server

    @Param Node $client
    '''
    for i in range(1, MAX_INDEX+1):
        # print('run')
        # print(i)

        node = get_bname(client, i)
        dict[node] = i
        # print(node, i)
        # print(node)


def mutate(node: object, mutation: dict):
    '''
    Mutates Input Node Variable Values.

    @Param Node $node
    @Param dict $mutation
    '''

    return 1


def get_node_value(node_name, server, dict):
    '''
    Get node value from server using dict[node_name]
    @Param
    String node_name - eg. Generation.Q1.
    Client server - a client to server.
    Dict dict - where the node is stored.
    '''
    # if 'MicroGrid.MIED1.Measurement.VL3_VL1' in node_name :
    #     print(server.get_node('ns=2;i={}'.format(
    #         dict[node_name])).get_value())

    return server.get_node('ns=2;i={}'.format(
        dict[node_name])).get_value()
