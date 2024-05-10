from flask import Flask, send_file
app = Flask(__name__)

@app.route('/rke-server-token')
def serve_text_file1():
    file_path= '/var/lib/rancher/rke2/server/token'
    return send_file(file_path,mimetype='text/plain')

@app.route('/rke-agent-token')
def serve_text_file2():
    file_path= '/var/lib/rancher/rke2/server/node-token'
    return send_file(file_path,mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
