# Python_gRPC_Project

This project focuses on utilizing gRPC, an open-source Remote Procedure Call developed by Google, to allow computers to access subroutines from computers in separate networks. By abstracting away the details of network communication, developers can build distributed applications more efficiently, with a focus on the logic of their applications.

## Setup

To use the program, first run the server.py file on the project directory.
```
python rover_server.py
```

Then, on a new terminal in the same directory, run the following command:

```
python rover_client.py {rover_num}
```
The rover_num can be any rover number from 1-10</br></br>

## Implementation
- The implementation builds from the the previous parallel vs concurrency project. Whenever the command is executed with the specified rover number, the client sends the request to the server. The server pre-processes the map.txt file into a matrix abstraction of type string and sends it back to the client. The client then processes the string into a traversable format, such as a list.

- The client requests the server again for the list of commands for the specified rover. The server receives this command, queries the API for the commands of the rover, and sends the list of moves to the client as a string.

- The client receives the moves and processes them into a list. It uses the traversal function implemented in Lab 1 to execute the commands. If a rover lands on a mine and does not dig on the next move, it will die.

- In this case, the client sends a status message to the server stating that the rover died. The server replies back with an acknowledgment, and the program ends.

- However, if the rover lands on a mine and digs on the next move, it will request the server for a random serial number. Once the server sends the serial number, the client finds the PIN to disarm the mine. It sends the PIN and the temporary mine hash to the server and moves to execute its next command.

- If the rover makes it to the end of its commands, it sends a status message to the server stating that it did not die. It receives an acknowledgment back from the server. 

## Sample Output
![](images/Picture_gRPC_Server.png)
<br/><br/><br/>
![](images/PicturegRPC_Client.png)



