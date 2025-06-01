from flask import Flask, request, render_template, send_from_directory
import logging
import os

app = Flask(__name__)

# Setup logging
http_logger = logging.getLogger('http_honeypot')
http_logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/http_logs.log')
http_logger.addHandler(fh)

@app.route('/', methods=['GET'])
def login_page():
    http_logger.info(f"[+] GET / - IP: {request.remote_addr}")
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        http_logger.info(f"[+] Admin Login Attempt - Username: {username} | Password: {password} | IP: {request.remote_addr}")
    else:
        http_logger.info(f"[+] GET /admin - IP: {request.remote_addr}")
    return render_template('admin.html')

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    fake_files_path = os.path.join(os.getcwd(), 'fake_files')
    http_logger.info(f"[+] Download Attempt - File: {filename} | IP: {request.remote_addr}")
    return send_from_directory(fake_files_path, filename, as_attachment=True)

def run_http_server():
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)

if __name__ == '__main__':
    run_http_server()
