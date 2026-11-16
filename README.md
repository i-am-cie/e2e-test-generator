# E2E Test Generator

> 本地AI端到端测试生成器，基于 Ollama 大模型，完全离线运行，无需 API Key。

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![LLM](https://img.shields.io/badge/LLM-Ollama-black)
![Offline](https://img.shields.io/badge/Offline-100%25-success)
![Tests](https://img.shields.io/badge/tests-7%20passed-success)

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

### 运行测试

仓库自带 pytest 单元测试（`tests/` 目录），覆盖 Selenium/Playwright/Page Object 三种生成方式的 prompt 拼装、模型调用参数和命令行框架分发。模型调用已打桩，运行测试无需启动 Ollama，也不依赖 `ollama` 包是否安装。

```bash
pip install -r requirements-dev.txt
python -m pytest tests/ -v
```

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
├── requirements.txt    # 运行依赖
├── requirements-dev.txt # 测试开发依赖（pytest）
├── tests/               # pytest 单元测试
└── README.md
```

## 🛠️ 技术栈

- **后端**：Python + Flask
- **LLM**：Ollama (Qwen2.5)
- **前端**：HTML + 原生 JS

## 说明

仓库自带的测试只覆盖 prompt 拼装和命令行分发代码，不会解析生成出来的测试脚本，也不校验模型产出的代码质量；脚本能否在真实浏览器跑通，仍需结合目标页面实际验证。

## 📝 License

MIT
