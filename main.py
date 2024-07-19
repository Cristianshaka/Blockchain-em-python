import hashlib


class NeuralCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        #concatena os blocos de string
        self.block_data = "-".join(transaction_list) + \
            "-" + previous_block_hash
        #gera a hash usando a função da bbiblioteca 
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

#transações
t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4.1 NC to Mike"
t3 = "Mike sends 3.2 NC to Bob"
t4 = "Daniel sends 6.3 NC to Anna"
t5 = "Mike sends 1 NC to Charlie"
t6 = "Mike sends 5.4 NC to Daniel"

#define os blocos
initial_block = NeuralCoinBlock("Initial string", [t1, t2])

#imprime cada bloco e hash
print(initial_block.block_data)
print(initial_block.block_data)
