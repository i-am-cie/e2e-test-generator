#!/usr/bin/env python3
"""
e2e-test-generator: Local AI E2E test script generator using Ollama.

Usage:
    python generator.py --desc "用户登录页面" --framework selenium
    python generator.py --desc "购物车功能" --framework playwright
"""

import argparse
import ollama

MODEL = "qwen2.5:7b"


def generate_selenium_script(description: str) -> str:
    """Generate Selenium E2E test script."""
    prompt = f"""你是一个资深自动化测试工程师。请根据以下需求生成Selenium自动化测试脚本。

需求描述：
{description}

要求：
1. 使用Python + Selenium WebDriver
2. 包含完整的测试步骤：打开浏览器、访问页面、操作元素、断言验证、关闭浏览器
3. 使用合理的CSS选择器或XPath定位元素
4. 包含正常场景和至少2个异常场景
5. 添加适当的注释说明每一步做什么
6. 使用pytest风格的函数组织

只输出Python代码，不要其他解释。
"""
    
    resp = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return resp["message"]["content"]


def generate_playwright_script(description: str) -> str:
    """Generate Playwright E2E test script."""
    prompt = f"""你是一个资深自动化测试工程师。请根据以下需求生成Playwright自动化测试脚本。

需求描述：
{description}

要求：
1. 使用Python + Playwright
2. 使用同步API（sync_playwright）
3. 包含完整的测试步骤：打开浏览器、访问页面、操作元素、断言验证
4. 使用get_by_role、get_by_text等推荐定位方式
5. 包含正常场景和至少2个异常场景
6. 添加适当的注释说明

只输出Python代码，不要其他解释。
"""
    
    resp = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return resp["message"]["content"]


def generate_page_object(page_name: str, description: str) -> str:
    """Generate Page Object class."""
    prompt = f"""你是一个资深自动化测试工程师。请为以下页面生成Page Object模式的Python类。

页面名称：{page_name}
页面描述：
{description}

要求：
1. 类名用PascalCase，比如LoginPage
2. 元素定位器作为类属性
3. 每个操作是一个类方法：输入用户名、点击登录按钮、获取错误提示等
4. 包含显式等待
5. 类型注解完整

只输出Python代码。
"""
    
    resp = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return resp["message"]["content"]


def main():
    parser = argparse.ArgumentParser(description="E2E Test Generator")
    parser.add_argument("--desc", type=str, required=True, help="功能描述")
    parser.add_argument("--framework", type=str, default="selenium", choices=["selenium", "playwright"], help="测试框架")
    
    args = parser.parse_args()
    
    if args.framework == "selenium":
        print(generate_selenium_script(args.desc))
    else:
        print(generate_playwright_script(args.desc))


if __name__ == "__main__":
    main()
