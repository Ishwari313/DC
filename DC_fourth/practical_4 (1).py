import random

# Servers
servers = [0, 0, 0]   # load on each server

# Generate client requests
requests = [random.randint(1, 10) for _ in range(10)]

# ---- Round Robin ----
def round_robin(requests, servers):
    loads = servers.copy()
    n = len(loads)
    sequence = [[] for _ in loads]
    for i, req in enumerate(requests):
        server = i % n
        loads[server] += req
        sequence[server].append(req)
    print(f'Round Robin Queue: {sequence}')
    return loads

# ---- Least Loaded ----
def least_loaded(requests, servers):
    loads = servers.copy()
    sequence = [[] for _ in loads]
    for req in requests:
        server = loads.index(min(loads))
        loads[server] += req
        sequence[server].append(req)
    print(f'\nLeast Loaded Queue: {sequence}')
    return loads

# ---- Random Allocation ----
def random_allocation(requests, servers):
    loads = servers.copy()
    sequence = [[] for _ in loads]
    for req in requests:
        server = random.randint(0, len(loads)-1)
        loads[server] += req
        sequence[server].append(req)
    print(f'\nRandom Allocation Queue: {sequence}')
    return loads

# ---- RUN ----
print("Requests:", requests, '\n')

print("Round Robin:", round_robin(requests, servers))
print("Least Loaded:", least_loaded(requests, servers))
print("Random:", random_allocation(requests, servers))
