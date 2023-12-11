import socket , sys , os , requests , split
# Os advice

# alegrarsio gifta l 

OS_advice = ""
if sys.platform.lower().startswith('win'): OS_advice += "Some feature may not available"
class get:
    def port(address , port_range):
        head = "Port Service\n"  
        print(head)
        for port in range(port_range[0] , port_range[1] + 1):
            try :
                s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                socket.gethostbyname(address)
                result = s.connect_ex((address , port))
                if result == 0:
                    body = "{p}".format(p = port),'{sn}'.format(sn = socket.getservbyport(port))
                    print(body,"\n")
                else : pass
            except KeyboardInterrupt : return "Process stopped"
            except socket.gaierror : raise socket.gaierror('Invalid IP address')
            except socket.herror : raise socket.herror('Server can not responded')
    def pyhttp(address , port):
        if address == 'a'.lower(): address = socket.gethostbyname(socket.gethostname())
        try : os.system('python -m http.server {p} -b {a}'.format(p = port , a = address))
        except KeyboardInterrupt : return "Process stoped"
        except OSError : return "Can not requet address"
    def clone(address):
        res = requests.get(address)
        html = res.text.encode('utf-8')
        file = open('index.html','w')
        file.write(html.decode('utf-8'))
    def html(address):
        res = requests.get(address)
        html = res.text
        return html      
    def iptype(address):
        types = ""
        if ('127' and 127 or '169' and 169) in address : types += "Private"
        if '.' in address and len(address[0] , address[1]) == 3 : 
            return "IPV4"
        elif ':' in address and len(address[0] , address[1]) > 3 : 
            return "IPV6"
        else : return "Can not scan ip address"
class sockserver :
    def main(address , port = int):
        try :
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            s.bind((address , port))
            while not False:
                client , addr = s.accept()
                s.close()                
        except KeyboardInterrupt: pass    
        except socket.gaierror: raise socket.gaierror('Invalid ip address')
        except socket.herror : raise socket.herror('Server can not responded')
    def client(address , port):
        try : 
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.connect((address , port))
            s.recv(1024)
        except socket.gaierror: return "Invalid IP address"
        except socket.herror : return "Server can not responded"        
class file:
    def remove(files):        
        try : os.remove(files)
        except FileNotFoundError : return "file not found"
    def write(title ,files):
        file = open(files,'w')
        file.write(title)
    def search(file):
        title = ""
        for i in os.listdir():
            if file in os.listdir():
                return "File Found for {f}".format(f = file)
            else : return "File not found for {f}".format(f = file)
    
