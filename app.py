from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None
    if request.method == 'POST':
        input_text = request.form.get('inputText')
        if input_text:
            img = qrcode.make(input_text)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            qr_code = f'data:image/png;base64,{img_base64}'
    return render_template('index.html', qr_code=qr_code)

# Optional: If you want to keep /generate as a separate route
@app.route('/generate', methods=['POST'])
def generate():
    input_text = request.form.get('inputText')
    qr_code = None
    if input_text:
        img = qrcode.make(input_text)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        qr_code = f'data:image/png;base64,{img_base64}'
    return render_template('index.html', qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True)