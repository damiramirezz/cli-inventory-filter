import argparse
from server import Server

def create_parser():
    parser = argparse.ArgumentParser(description = """
    Allows the user to retrieve a sub set of the devices, filtered by any or a combination of the characteristics defined in the naming standard
    """)
    parser.add_argument('-f', help = 'file to read', type = str.lower)
    parser.add_argument('-i', help = 'id of the server', type = int)
    parser.add_argument('-k', help = 'task of the server', type = str.lower)
    parser.add_argument('-e', help = 'env of the server', type = str.lower)
    parser.add_argument('-l', help = 'location of the server', type = str.lower)
    parser.add_argument('-t', help = 'team of the server', type = str.lower)
    return parser

args = create_parser().parse_args()

server_list = []

try:
    with open(args.f, 'r') as f:
        for line in f:
            # Split the string to be able to create the class
            server_split = line.split('.')
            team_split = server_split[4].split('/')[0].strip()
            server_split[4] = team_split

            # Create server class
            server = Server(int(server_split[0]), server_split[1], server_split[2],server_split[3], server_split[4])
            server_list.append(server)

except FileNotFoundError as err:
    print('File not found!')
    print(err)

except TypeError as err:
    print('No file was passed by attribute')
    print(err)

# Filter options
if args.i:
    server_list = filter(lambda server: server.id == args.i, server_list)
if args.k:
    server_list = filter(lambda server: server.task == args.k, server_list)
if args.e:
    server_list = filter(lambda server: server.environment == args.e, server_list)
if args.l:
    server_list = filter(lambda server: server.location == args.l, server_list)
if args.t:
    server_list = filter(lambda server: args.t == server.team, server_list)

# Print the server list
for server in server_list:
    print(server, end = '')