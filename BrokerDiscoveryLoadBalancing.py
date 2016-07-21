MAX_CONNECTIONS = 20

class Broker(object):
    def __init__(self,brokerName,brokerIP):
        self.Name=brokerName
        self.IP=brokerIP
        self.num_connections = 0

class BrokerDiscoveryLoadBalancing(object):
    def __init__(self):
        self.connection_map = {}
        self.brokers = []

    def register_broker(self, brokerName, brokerIP):
        self.brokers.append(Broker(brokerName, brokerIP))
        self.connection_map[brokerIP] = 0

    def insert_connection(self, brokerIP):
        try:
            self.connection_map[brokerIP] += 1
        except:
            self.connection_map[brokerIP] = 1

    def remove_connection(self, brokerIP):
        try:
            self.connection_map[brokerIP] -= 1
        except:
            print "Broker does not exist. Something went wrong"

    def get_least_connected_broker(self):
        pass
