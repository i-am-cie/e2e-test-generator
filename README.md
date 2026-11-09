# E2E Test Generator

> 本地AI端到端测试生成器，基于 Ollama 大模型，完全离线运行，无需 API Key。

## ✨ 功能特性

- **从需求生成脚本**：输入用户故事/页面描述，自动生成Selenium/Playwright自动化测试代码
- **多框架支持**：输出Python+Selenium / Python+Playwright两种格式
- **元素定位**：AI自动生成合理的CSS选择器/XPath
- **测试步骤**：包含打开页面、操作元素、断言验证、异常场景
- **Page Object模式**：生成规范的PO结构，可直接用于项目
- **完全本地**：所有数据都在你的电脑上

## 🚀 快速开始

### 前置要求

1. 安装 [Ollama](https://ollama.com/)
2. 拉取模型：
   ```bash
   ollama pull qwen2.5:7b
   ```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动 Web 界面

```bash
python app.py
```

打开浏览器访问 http://localhost:5004

### 命令行模式

```bash
# 生成Selenium脚本
python generator.py --desc "用户登录页面：输入用户名密码，点击登录按钮，验证跳转到首页" --framework selenium

# 生成Playwright脚本
python generator.py --desc "购物车功能：添加商品，修改数量，删除商品" --framework playwright
```

## 📦 项目结构

```
e2e-test-generator/
├── app.py              # Flask Web 界面
├── generator.py        # 核心脚本生成逻辑
├── requirements.txt    # Python 依赖
└── README.md
```

## 🛠️ 技术栈

- **后端**：Python + Flask
- **LLM**：Ollama (Qwen2.5)
- **前端**：HTML + 原生 JS

## 📝 License

MIT