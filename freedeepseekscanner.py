import requests
import json
import sys
import argparse


def check_ollama_service(url):
    try:
        # 检查Ollama是否在运行
        response = requests.get(url)
        if "Ollama is running" in response.text:
            print(f"Ollama服务正在运行: {url}")

            # 拼接/api/tags并访问
            api_url = f"{url.rstrip('/')}/api/tags"
            api_response = requests.get(api_url)

            if api_response.status_code == 200:
                # 解析模型信息
                models = json.loads(api_response.text)
                if models.get("models"):
                    print("检测到的模型:")
                    for model in models["models"]:
                        print(
                            f"- {model.get('name')} (大小: {model.get('size')} bytes)"
                        )
                else:
                    print("未检测到任何模型")
            else:
                print(f"无法获取模型信息，HTTP状态码: {api_response.status_code}")
        else:
            print(f"未检测到Ollama服务: {url}")

    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")


def main():
    parser = argparse.ArgumentParser(description="Deepseek模型服务扫描器")
    parser.add_argument("urls", nargs="+", help="要扫描的URL列表")

    args = parser.parse_args()

    for url in args.urls:
        print(f"\n正在扫描: {url}")
        check_ollama_service(url)


if __name__ == "__main__":
    main()
