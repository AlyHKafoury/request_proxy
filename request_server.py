import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8010)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(20480)
            print >>sys.stderr, 'received "%s"' % repr(data)
            if len(data) > 3:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            	if data[-4:] == "\r\n\r\n":
                	print >>sys.stderr, 'no more data from', client_address
			sock.close()
        		connection.close()
                	break
	    else:
	        break
            
    finally:
        # Clean up the connection
	sock.close()
        connection.close()
    break

