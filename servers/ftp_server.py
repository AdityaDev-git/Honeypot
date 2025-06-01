from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    authorizer = DummyAuthorizer()

    # Add a user with full permissions (fake user for honeypot)
    authorizer.add_user("admin", "admin123", ".", perm="elradfmwMT")

    handler = FTPHandler
    handler.authorizer = authorizer

    # Enable logging login attempts
    def on_login_failed(self, username, password):
        print(f"[!] Failed login - Username: {username}, Password: {password}")

    handler.on_login_failed = on_login_failed

    server = FTPServer(("0.0.0.0", 2121), handler)
    print("[+] FTP Server started on port 2121")
    server.serve_forever()
