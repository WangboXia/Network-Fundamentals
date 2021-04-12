from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)
# wait up to one second for a reply
clientSocket.settimeout(1)

server_address = ('172.19.121.245', 12000) # network port

trip_time_list = []
error_count = 0

for sequence_number in range(1, 11):
    # The ping messages in this lab are formatted:
    # Ping sequence_number time
    message = "Ping %d %d" % (sequence_number, time.time())
    try:
        # send the ping message using UDP
        clientSocket.sendto(message.encode(), server_address)
        # receive server echo message
        message, address = clientSocket.recvfrom(1024)#port number
        if address == server_address:
            message = message.decode()
            # print the response message
            print(message)
            # calculate and print the round trip time (RTT), in seconds
            tokens = message.split()
            start_time = int(tokens[2])  # PING 2 1526960157
            trip_time = (time.time() - start_time) / 1000.0  # round trip time
            trip_time_list.append(trip_time)
            print("\tRTT:", trip_time, "seconds")#RTT: Rround trip time
    except OSError:
        error_count += 1
        print("Request timed out")

if len(trip_time_list) > 0: # ( optional )
    print("maximum trip time: ", max(trip_time_list))
    print("minimum trip time: ", min(trip_time_list))
    print("average trip time: ", sum(trip_time_list) / len(trip_time_list))
print("packet loss rate: ", error_count / 10.0 * 100, "%")
