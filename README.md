The CLI internet chat interface

Uses Python 2.7.6
No additional modules used

Steps:

1) Start the server:
	python chat_server.py

2) Open a new terminal or copy the application folder on a remote machine

3) Start the client requests:
	python chat_client.py

4) The client is an interactive chat & will be prompted for:
	a) Name
	b) Message type : cmd or msg
	c) Message

5) The message will be sent to the server 
6) The server will check for the below cases:
	a) If the message is of type cmd execute it:
		i) Check the EXIT code of the command
		ii) Return an 'ACK' if the cmd is syntactically correct (EXIT code = 0)
		iii) Catch the exception in cmd error (EXIT code other than 0) & return 'NOACK')

	b) If the message is of type msg:
		i) Return 'ACK' to client

	c) If the Client sent a 'q'; means the client/user left the chat
	d) If the Client sent a 'Quit'; the server will be stopped (In this case a single worker) 

