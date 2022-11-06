from pprint import pprint

pprint([{'dec': num, 'bin': bin(num), 'oct': oct(num), 'hex': hex(num)} for num in range(16)])
