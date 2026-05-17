import rpyc

conn = rpyc.connect("localhost", 18861)

n = int(input("Enter number: "))
result = conn.root.factorial(n)

print("Factorial:", result)
