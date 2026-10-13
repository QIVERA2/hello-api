# hello-api

用 FastAPI 写的待办事项 REST API，带自动生成的交互式接口文档。

这是我系统学习 Python 工程化 + AI 应用开发的第一个练手项目，后续会持续迭代。

## 功能

- 新增 / 查询待办项（完整 CRUD 的基础链路）
- 请求体与响应数据的自动校验（Pydantic）
- 自动生成的 Swagger UI 接口文档，可直接在页面里试调用
- 健康检查端点，便于后续部署时探活

## 技术栈

| 用途 | 选型 |
|---|---|
| Web 框架 | FastAPI 0.143 |
| ASGI 服务器 | uvicorn 0.54 |
| 数据校验 | Pydantic |
| 包管理 | uv |
| Python | 3.13 |

## 快速开始

```bash
# 进入项目目录后
uv venv
uv pip install fastapi uvicorn

# 启动（--reload 改代码自动重启）
uvicorn main:app --reload
```

启动后浏览器打开 <http://127.0.0.1:8000/docs>，能看到 FastAPI 自动生成的接口文档，可以直接在页面上点「Try it out」测试每个接口。

## 接口一览

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/` | 欢迎信息，确认服务已启动 |
| GET | `/health` | 健康检查 |
| POST | `/items` | 新增待办项 |
| GET | `/items` | 查看全部待办项 |

## 项目结构

```
hello-api/
├── main.py           # 应用入口与路由定义
├── .env.example      # 环境变量模板（复制为 .env 后填入自己的 key）
└── .gitignore        # 排除 .env、.venv 等，防止密钥外泄
```

## 后续计划

- [ ] 接入 SQLite / PostgreSQL 做持久化，替换当前的内存存储
- [ ] 加入用户认证
- [ ] 补单元测试与集成测试
- [ ] Docker 化并部署到公网
