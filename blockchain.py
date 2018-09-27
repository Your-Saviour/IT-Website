import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from usertest import *
from pprint import *
import requests
from flask import Flask, jsonify, request, render_template

class Blockchain:
    def __init__(self, userchain):
        self.current_transactions = []
        self.chain = []
        self.nodes = set()

        # Create the genesis block
        self.new_block(previous_hash='1', proof=100)


    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        """
        Simple Proof of Work Algorithm:

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof

        :param last_block: <dict> last Block
        :return: <int>
        """

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    def vaild_transaction(self, sender, recipient, private_key):
        user.is_private_valid()

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        """
        Validates the Proof

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.

        """

        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


# Instantiate the Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
users = Userchain()
blockchain = Blockchain(users)
app.secret_key = 'iaLjhsAiGIywsIwLqUeCoJygdqWACMJMjEcejbcDBUaYmyhWqbIzFyeaowaTobrZWhaFnLRWppduOhnMeCNXRslhfNujJBfHlOzV'
session['logged_in'] = False

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount', 'sender_private']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/page')
def login():
    return render_template('loginnew.html')
@app.route("/loginsend", method=["POST"])
def loginincheck():
    email = request.form.get('email')
    password = request.form.get('password')
    if users.login(email, password):
        return redirect('/page2')

@app.route('/page2')
def mainpage():
    return render_template('Main.html', name="Jake Townend", balence="$0", public_key_page="rctfvgbhyvuyvu", privatekey="TVVUYVUVYUVYUVYUVUY", transactions=["$2", "$5", "$10"])



if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    names = ["Mamie Waugh", "Samatha Dana", "Ka Wayland", "Josphine Gustafson", "Martin Stanford", "Angeline Gillespi", "Brittny Ness", "Cleveland Ponte", "Abdul Buchler", "Renea Phu", "Sha Wilhoit", "Jackeline Mcglinchey", "Quinton Wimberley", "Jacquelin Amann", "Brain Cooperman", "Diana Sheffer", "Laree Steadman", "Carla Fortenberry", "Serita Sherk", "Bettie Stites", "Deloris Lorence", "Lemuel Volkert", "Carmelo Fallen", "Genia Schneider", "Lieselotte Nemeth", "Shani Celestin", "Gertie Alba",
    "Millie Niblett", "Sade Fusaro", "Corrie Gorgone", "Lucila Teske", "Elfriede Curnutte", "Malcom Royals", "Alise Hermansen", "Tama Brocious", "Hanh Alphin", "Reinaldo Swan", "Mariel Rumore", "Daisy Schmid", "Bobbie Frankum", "Henriette Darbonne", "Inge Montufar", "Alline Gourlay", "Gilberto Geers", "Dalila Petersen", "Shanel Caro", "Towanda Manning", "Marsha Rayburn", "Wiley Keesee", "Destiny Kendrick"]
    for i in range(50):
        current_name = random.choice(names)
        current_name = current_name.split()
        users.adduser(current_name[0], '{}{}@gmail.com'.format(current_name[0], current_name[1]), current_name[1])
    pprint(users.getusers())
    app.run(debug=True,host='0.0.0.0', port=port)
