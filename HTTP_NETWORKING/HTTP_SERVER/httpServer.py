from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

#Task list which are present
tasklist=["tak1","I have to go market","Task3"]

class requestHandler(BaseHTTPRequestHandler):
    #setting the headers
    def _set_headers(self):
        #Adds a response header to the headers buffer and logs the accepted request
        self.send_response(200)
        #Adds the HTTP header to an internal buffer 
        #which will be written to the output stream when either end_headers() or flush_headers() is invoked
        self.send_header('Content-type', 'text/html')
        #Adds a blank line (indicating the end of the HTTP headers in the response) 
        #to the headers buffer and calls flush_headers().
        self.end_headers()

    #GET METHOD 
    def do_GET(self):
        self._set_headers()
        #will check whether the URL ends with /tasklist and then show all the task
        if self.path.endswith('/tasklist'):
            #output append
            output=""
            output+="<html><body>"
            output+="<h1>Task list</h1>"
            output+="<h3><a href='/tasklist/new'>Add New Task</a></h3>"
            for task in tasklist:
                output+=task
                output+="<a href='/tasklist/"
                output+=task
                output+="/delete' style='margin-right:20px;text-decoration:none'>(X)</a>"
                output+="<br/>"
            output+="</body></html>"
            #Contains the output stream for writing a response back to the client
            self.wfile.write(output.encode())

         #will check whether the URL ends with /new and adds new task to the task list
        if self.path.endswith('/new'):
             output=""
             output+="<html><body>"
             output+="<h1>Add new Task</h1>"
             output+="<form method='POST' enctype='multipart/form-data' action='/tasklist/new'>"
             output+='<input type="text" name="task" id="" placeholder="Add Task"><br/><br/>'
             output+='<input type="submit" value="Submit"></form>'
             output+='</body></html>'
             self.wfile.write(output.encode())

        #will check whether the URL ends with /delete and deletes the task from the task list
        if self.path.endswith("/delete"):
            listId=self.path.split("/")[2].replace('%20', ' ')
            output=""
            output+="<html><body>"
            output+="<h1>Remove Task:"
            output+=listId
            output+="</h1>"
            output+="<form method='POST' enctype='multipart/form-data' action='/tasklist/"
            output+=listId
            output+="/delete'>"
            output+='<input type="submit" value="Remove this task"></form>'
            output+='<a href="/tasklist">Cancel</a>'
            output+='</body></html>'
            self.wfile.write(output.encode())



    #POST method
    #his method serves the 'POST' request type, only allowed for CGI scripts
    def do_POST(self):
        #path that ends with /new
        #for posting the new task
        if self.path.endswith('/new'):
            #Commmon gateway interface (cgi) for parsing the user input
            ctype,pdict=cgi.parse_header(self.headers["Content-Type"])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype=="multipart/form-data":
                fields=cgi.parse_multipart(self.rfile,pdict)
                new_task=fields.get("task")
                tasklist.append(new_task[0])
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            #redirecting to the /tasklist after new task is added
            self.send_header("location","/tasklist")
            self.end_headers()
        
        #path endswith delete
        if self.path.endswith("delete"):
            #yaking out the listID
            listId=self.path.split("/")[2].replace("%20"," ")
            ctype,pdict=cgi.parse_header(self.headers["Content-Type"])
            if ctype=="multipart/form-data":
                list_item=listId
                tasklist.remove(list_item)
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            #redirecting to the /tasklist after task deleted
            self.send_header("location","/tasklist")
            self.end_headers()

       
def main():
    PORT=3000
    server=HTTPServer(("",PORT),requestHandler)
    print("Server running on port "+str(PORT))
    server.serve_forever()

if __name__ == "__main__":
    main()


