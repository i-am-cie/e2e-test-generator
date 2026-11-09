#!/usr/bin/env python3
"""
e2e-test-generator Web UI (Flask)
"""

from flask import Flask, render_template_string, request, jsonify
from generator import generate_selenium_script, generate_playwright_script, generate_page_object

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E2E Test Generator</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1100px; margin: 0 auto; }
        h1 { color: white; text-align: center; margin-bottom: 30px; font-size: 2.5rem; }
        .card {
            background: white;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        .step { margin-bottom: 25px; }
        .step-title { font-size: 1.2rem; font-weight: bold; color: #333; margin-bottom: 10px; }
        textarea {
            width: 100%;
            min-height: 100px;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            font-family: 'Courier New', monospace;
            resize: vertical;
        }
        textarea:focus { outline: none; border-color: #667eea; }
        select {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            margin-bottom: 15px;
        }
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover { transform: translateY(-2px); }
        .result {
            margin-top: 20px;
            padding: 20px;
            background: #1e1e1e;
            color: #d4d4d4;
            border-radius: 8px;
            white-space: pre-wrap;
            display: none;
            line-height: 1.6;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            overflow-x: auto;
        }
        .result.show { display: block; }
        .loading { text-align: center; display: none; padding: 20px; }
        .loading.show { display: block; }
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 E2E Test Generator</h1>
        
        <div class="card">
            <div class="step">
                <div class="step-title">1. 描述你要测试的功能</div>
                <textarea id="desc" placeholder="例如：用户登录页面：输入用户名密码，点击登录按钮，验证跳转到首页。错误密码时显示提示信息。"></textarea>
            </div>

            <div class="step">
                <div class="step-title">2. 选择测试框架</div>
                <select id="framework">
                    <option value="selenium">Selenium (Python)</option>
                    <option value="playwright">Playwright (Python)</option>
                </select>
            </div>

            <button onclick="generate()">生成测试脚本</button>

            <div class="loading" id="loading">
                <div class="spinner"></div>
                <p>AI 正在生成测试脚本...</p>
            </div>

            <div class="result" id="result"></div>
        </div>
    </div>

    <script>
        async function generate() {
            const desc = document.getElementById('desc').value;
            const framework = document.getElementById('framework').value;
            
            if (!desc.trim()) { alert('请输入功能描述'); return; }
            
            document.getElementById('loading').classList.add('show');
            document.getElementById('result').classList.remove('show');
            
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({desc, framework})
            });
            
            const data = await response.json();
            
            document.getElementById('loading').classList.remove('show');
            document.getElementById('result').textContent = data.result;
            document.getElementById('result').classList.add('show');
        }
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/generate', methods=['POST'])
def api_generate():
    data = request.json
    desc = data.get('desc', '')
    framework = data.get('framework', 'selenium')
    
    if framework == 'selenium':
        result = generate_selenium_script(desc)
    else:
        result = generate_playwright_script(desc)
    
    return jsonify({'result': result})


if __name__ == '__main__':
    print("🤖 E2E Test Generator 启动中...")
    print("📖 访问 http://localhost:5004")
    app.run(debug=True, port=5004)
