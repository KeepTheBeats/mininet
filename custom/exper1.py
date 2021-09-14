from mininet.topo import Topo


class exper1Topo(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add hosts and switches
        Host1 = self.addHost("h1")
        Host2 = self.addHost("h2")
        Host3 = self.addHost("h3")
        Switch1 = self.addSwitch("s1")
        Switch2 = self.addSwitch("s2")

        # Add links
        self.addLink(Host1, Switch1)
        self.addLink(Host2, Switch1)
        self.addLink(Host3, Switch2)
        self.addLink(Switch1, Switch2)


topos = {"exper1": (lambda: exper1Topo())}
