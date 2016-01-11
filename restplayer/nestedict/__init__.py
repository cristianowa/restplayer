children = "children"
name = "name"
value = "value"

class Nestedict(dict):
    def __init__(self, nome, val, delimiter="/"):
        super(dict, self).__init__()
        self.delimiter = delimiter
        self[children] = []
        self.add_node(nome, val)

        #self[name] = name
    def add_node(self, nome, val):
        address = nome.split(self.delimiter)
        nome = address[-1:][0]
        address = address[:-1]
        if len(address) == 0:
            self[name] = nome
            self[value] = val
        else:
            for child in self[children]:
                if len(address) > 1 and child[name] == address[1]:
                    child[children].append(Nestedict(self.delimiter.join(address[2:] + [nome]), val))
                    return
            self[children].append(Nestedict(self.delimiter.join(address[1:] + [nome]), val))
            self[name] = address[0]
