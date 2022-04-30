
import random
import sympy
import time

class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def push(self, data):
        if not self.data:
            self.data = data
            return
        if data < self.data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.push(data)
        elif data > self.data:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.push(data)

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def coprime(n):
	j=1
	for i in range(2,(n-1)):
		if gcd(n,i) == 1:
			j = i
	return j

def is_coprime(x, y):
    return gcd(x, y) == 1

def generate():
    p1 = sympy.randprime(10000, 100000)
    p2 = sympy.randprime(10000, 100000)
    print("P1 and P2 is coprime? = {}".format(is_coprime(p1,p2)))
    n = p1*p2
    phi = (p1-1) * (p2-1)
    e = coprime(phi)

    # pow ถ้า e = 38 , phi = 97, 23 = 23*38%97 = 1 ,multiplicative inverse
    d = pow(e, -1, phi)
    return n, e, d

def inlist(array):
    for i in range(len(array)):
        value = array[i]
        print("M = {}".format(value))
        encrypted = pow(value,e,n)
        decrypted = pow(encrypted,d,n)

        print("Encrypted = {}".format(encrypted))
        print("Decrypted = {}".format(decrypted))
        print("Public key = {} {}".format(e, n))
        print("Private key = {} {}".format(d, n))
        print("n = {} : e = {} : d = {}\n".format(n,e,d))

def binary_tree(array):
    tree = Tree()
    for i in range(len(array)):
        value = array[i]
        encrypted = pow(value,e,n)
        decrypted = pow(encrypted,d,n)
        data = ["M = {}".format(value),"Encrypted = {}".format(encrypted),"Decrypted = {}".format(decrypted)]
        tree.push(data)
    tree.print()
        

if __name__ == "__main__":
    array = [random.randint(10000, 100000) for _ in range(10)]
    print(array)
    [n, e, d] = generate()
    start = time.time()
    inlist(array)
    list_end = time.time() - start
    print("Binary Tree")
    start = time.time()
    binary_tree(array)
    tree_end = time.time() - start
    print(f"list used: {list_end} ms")
    print(f"tree used: {tree_end} ms")
    print(f'{ "tree" if list_end > tree_end else "list"} is faster.')