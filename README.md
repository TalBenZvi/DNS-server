# DNS-server
Maps domain names to IP adresses
<br>
- The server recieves a domain as input and sends the corresponding IP adress as output
- Input and output sent using UDP, not the command line
- Known IP adresses are saved in a text file as well as a TTL
- If the server can't find an IP adress it will ask it's parent server and keep the answer
<br>

## Command line Argument and Server Hierarchy
Run the code several times simultaneously to create a functioning server hierarchy. <br>
<br> 
Command line arguments: <br>
[myPort] [parentIP] [parentPort] [ipsFileName] <br>
<br>
*parentIP and parentPort are -1 for the root server
<br> <br>

## Testing
Test the server using the provided 'client.py', type your requested domain and recieve the IP adress throught the command line. For your convenience, an example IP's text file is also provided.  
