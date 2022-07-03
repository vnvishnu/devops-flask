from flask import Flask
app = Flask(__name__)

@app.route("/")
import socket
def get_Host_name_IP():
	try:
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		print("Hostname : ",host_name)
		print("IP : ",host_ip)
	except:
		print("Unable to get Hostname and IP"
if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000)
