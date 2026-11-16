"""
generator.py 的单元测试。

ollama 调用通过 unittest.mock 打桩，测试不发起真实模型请求，
也不依赖 ollama Python 包是否安装（见 conftest.py）。
覆盖：模型调用契约、Selenium/Playwright/Page Object 的 prompt 拼装、命令行分发。
"""

import sys
from unittest.mock import MagicMock, patch

import generator as g


def _fake_ollama(content: str) -> MagicMock:
    return MagicMock(return_value={"message": {"content": content}})


def _captured_prompt(mock_chat: MagicMock) -> str:
    return mock_chat.call_args.kwargs["messages"][0]["content"]


# ---------- 模型调用契约 + prompt 拼装 ----------

def test_selenium_prompt_includes_description():
    description = "用户登录页面：输入用户名密码，点击登录按钮"
    mock_chat = _fake_ollama("selenium脚本")
    with patch.object(g.ollama, "chat", mock_chat):
        result = g.generate_selenium_script(description)

    assert result == "selenium脚本"
    prompt = _captured_prompt(mock_chat)
    assert description in prompt
    assert "Selenium WebDriver" in prompt


def test_playwright_prompt_includes_description():
    description = "购物车功能：添加商品，修改数量，删除商品"
    mock_chat = _fake_ollama("playwright脚本")
    with patch.object(g.ollama, "chat", mock_chat):
        result = g.generate_playwright_script(description)

    assert result == "playwright脚本"
    prompt = _captured_prompt(mock_chat)
    assert description in prompt
    assert "sync_playwright" in prompt


def test_page_object_prompt_includes_page_name_and_description():
    mock_chat = _fake_ollama("PO类代码")
    with patch.object(g.ollama, "chat", mock_chat):
        result = g.generate_page_object("LoginPage", "登录页：用户名、密码、登录按钮、错误提示")

    assert result == "PO类代码"
    prompt = _captured_prompt(mock_chat)
    assert "LoginPage" in prompt
    assert "登录页：用户名、密码、登录按钮、错误提示" in prompt
    assert "PascalCase" in prompt


def test_each_call_uses_configured_model():
    mock_chat = _fake_ollama("ok")
    with patch.object(g.ollama, "chat", mock_chat):
        g.generate_selenium_script("登录页面")
    assert mock_chat.call_args.kwargs["model"] == g.MODEL


# ---------- main() 命令行分发 ----------

def test_main_selenium_framework_calls_selenium_script():
    with patch.object(g, "generate_selenium_script") as mock_se, \
         patch.object(g, "generate_playwright_script") as mock_pw, \
         patch.object(sys, "argv", ["generator.py", "--desc", "登录页面", "--framework", "selenium"]):
        g.main()
    mock_se.assert_called_once_with("登录页面")
    mock_pw.assert_not_called()


def test_main_playwright_framework_calls_playwright_script():
    with patch.object(g, "generate_selenium_script") as mock_se, \
         patch.object(g, "generate_playwright_script") as mock_pw, \
         patch.object(sys, "argv", ["generator.py", "--desc", "购物车", "--framework", "playwright"]):
        g.main()
    mock_pw.assert_called_once_with("购物车")
    mock_se.assert_not_called()


def test_main_default_framework_is_selenium():
    with patch.object(g, "generate_selenium_script") as mock_se, \
         patch.object(g, "generate_playwright_script") as mock_pw, \
         patch.object(sys, "argv", ["generator.py", "--desc", "登录页面"]):
        g.main()
    mock_se.assert_called_once_with("登录页面")
    mock_pw.assert_not_called()
