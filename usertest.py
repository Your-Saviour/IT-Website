import hashlib
import secrets
import string
from pprint import pprint
import random
class Userchain:
    def __init__(self):
        self.chain = {}
        self.public_key = []
        self.private_key = []

    def adduser(self, name, email, password):
        #generating public key


        list_of_random_numbers =[]

        #new_number = random.randint(0,1000)
        #while new_number in list_of_random_numbers:
            #new_number = random.randint(0,1000)


        public_key = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(64))
        self.public_key.append(public_key)
        #while public_key in self.public_key:
            #public_key = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(64))
            #self.public_key.append(public_key)
        private_key = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(64))
        self.private_key.append(private_key)
        #while private_key in self.private_key:
            #private_key = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(64))


        password = password.encode('utf-8')
        #
        #print(password)
        self.chain[name] = {
            'name': name,
            'email': email,
            'password': str(hashlib.sha256(password).hexdigest()),
            'public key': public_key,
            'private key': private_key,
            'balence': 0
        }
        return self.chain[name]

    def getusers(self):
        return self.chain

    def get_public(self, name):
        return self.chain[name]['public key']

    def get_name(self, email):
        for user in self.chain:
            if self.chain[user]['email'] == str(email):
                return self.chain[user]['name']

    def get_private(self, name):
        return self.chain[name]['private key']

    def get_balence(self, name):
        return self.chain[name]['balence']

    def is_public(self, public_key):
        if public_key in self.public_key:
            return True
        else:
            return False

    def is_private(self, private_key):
        if private_key in self.private_key:
            return True
        else:
            return False

    def is_private_valid(self, private_key, public_key):
        for user in self.chain:
            if self.chain[user]['public key'] == public_key:
                return [self.chain[user]['private key'], self.chain[user]['name']]

    def vaild_transaction(self, public_key, private_key, name):
        if not name in self.chain:
            #return "Name not in chain"
            return False

        if self.chain[name]['public key'] != public_key:
            #return "Public Key not found"
            return False

        if self.chain[name]['private key'] != private_key:
            #return "Private key doesnt match"
            return False

        if self.chain[name]['public key'] == public_key:
            if self.chain[name]['private key'] == private_key:
                    return True
        return False

    def login(self, email, password):
        password = password.encode('utf-8')
        password = str(hashlib.sha256(password).hexdigest())
        for user in self.chain:
            if self.chain[user]['email'] == str(email) and self.chain[user]['password'] == str(password):
                return True
        #return False

    def balence_update(self, pubkey, amount):
        final = 0
        for i in amount:
            final = final + int(i)
        for user in self.chain:
            if self.chain[user]["public key"] == pubkey:
                self.chain[user]["balence"] = final


if __name__ == '__main__':
    names = ["Mamie Waugh", "Samatha Dana", "Ka Wayland", "Josphine Gustafson", "Martin Stanford", "Angeline Gillespi", "Brittny Ness", "Cleveland Ponte", "Abdul Buchler", "Renea Phu", "Sha Wilhoit", "Jackeline Mcglinchey", "Quinton Wimberley", "Jacquelin Amann", "Brain Cooperman", "Diana Sheffer", "Laree Steadman", "Carla Fortenberry", "Serita Sherk", "Bettie Stites", "Deloris Lorence", "Lemuel Volkert", "Carmelo Fallen", "Genia Schneider", "Lieselotte Nemeth", "Shani Celestin", "Gertie Alba",
    "Millie Niblett", "Sade Fusaro", "Corrie Gorgone", "Lucila Teske", "Elfriede Curnutte", "Malcom Royals", "Alise Hermansen", "Tama Brocious", "Hanh Alphin", "Reinaldo Swan", "Mariel Rumore", "Daisy Schmid", "Bobbie Frankum", "Henriette Darbonne", "Inge Montufar", "Alline Gourlay", "Gilberto Geers", "Dalila Petersen", "Shanel Caro", "Towanda Manning", "Marsha Rayburn", "Wiley Keesee", "Destiny Kendrick"]
    print(random.choice(names))
    userchain = Userchain()
    for i in range(50):
        current_name = random.choice(names)
        current_name = current_name.split()
        userchain.adduser(current_name[0], '{}{}@gmail.com'.format(current_name[0], current_name[1]), current_name[1])

    userchain.adduser('Jake', 'jake2townsend@gmail.com', 'noot')
    userchain.adduser('Not Jake', 'KGHVHVKHJCGGIUVYHCVY', 'iahpsdguvasvdhj')
    pprint(userchain.getusers())
    #jakepublic = userchain.get_public('Jake')
    #jakeprivate = userchain.get_private('Jake')
    #print(userchain.get_public('Jake'))
    #print(userchain.is_private_valid(jakeprivate, jakepublic))
    #print("DONE")
