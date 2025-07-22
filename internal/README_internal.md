```
|---internal // 应用所有内部文件夹
| ├---core // LLM核心文件，集成LangChain、LLM、Embedding等非逻辑的代码
| ├---exception // 通用公共异常目录
| ├---extension // Flask扩展文件目录
| ├---handler // 路由处理器、控制器目录
| ├---middleware // 应用中间件目录，包含校验是否登录
| ├---migration // 数据库迁移文件目录，自动生成
| ├---model // 数据库模型文件目录
| ├---router // 应用路由文件夹
| ├---schedule // 调度任务、定时任务文件夹
| ├---schema // 请求和响应的结构体
| ├---server // 构建的应用，与app文件夹对应
| ├---service // 服务层文件夹
| ├---task // 任务文件夹，支持即时任务+延迟任务
```