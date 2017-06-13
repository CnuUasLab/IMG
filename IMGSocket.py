import socket
import os
import thread

class IMGSocket():
    def __init__(self):
        self.server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("", 5005))
        self.server.listen(5)
        
        self.client_socket, self.address = server_socket.accept()
        
        # Start socket stream on server.
        thread.start_new_thread(self.startSocketStream, ())

    def startSocketStream(self):
        while(True):
            data = client_socket.recv(1024)
            print "The following data was received - ",data
            print "Opening file - ",data
            img = open(data,'r')
            while True:
                strng = img.readline(512)
                if not strng:
                    break
                client_socket.send(strng)
            img.close()
            print "Data sent successfully"
            exit()
            #data = 'viewnior '+data
            #os.system(data)
