# Deepseek 模型服务扫描器

## 概述
这是一个用于扫描公网暴露的Deepseek模型服务的Python工具。它能够检测运行Ollama服务的服务器，并列出可用的模型信息。

## 漏洞原理
该工具利用了一个安全漏洞：当Ollama服务未正确配置访问控制时，任何用户都可以通过HTTP请求访问`/api/tags`端点，获取服务器上运行的所有模型信息。这种信息泄露可能导致以下风险：
1. 暴露内部使用的AI模型
2. 泄露模型大小等敏感信息
3. 为攻击者提供目标系统的详细信息

## 安装
1. 确保已安装Python 3.x
2. 安装依赖：
   ```bash
   pip install requests
   ```

## 使用方法
```bash
python freedeepseekscanner.py [URL1] [URL2] ...
```

### 示例
扫描单个URL：
```bash
python freedeepseekscanner.py http://example.com:9009
```

扫描多个URL：
```bash
python freedeepseekscanner.py http://example1.com:9009 http://example2.com:11434
```

## 输出示例
```
正在扫描: http://example.com:9009
Ollama服务正在运行: http://example.com:9009
检测到的模型:
- deepseek-r1:32b (大小: 19851337640 bytes)
```

## 注意事项
1. 请仅对您有权扫描的服务器使用此工具
2. 该工具仅用于安全测试和教育目的
3. 如果发现暴露的Ollama服务，请及时通知相关管理员

## 贡献
欢迎提交Pull Request或Issue来改进本项目

## 许可证
MIT License
