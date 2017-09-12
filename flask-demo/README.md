## Docker部署flask应用Demo

#### 构建镜像
```shell
cd flask-demo
docker build -t eb-py-sample:v1 .
```

#### 运行镜像
```
# 将宿主机的8000端口暴露给容器的5000端口
docker run -d -p 8000:5000 eb-py-sample:v1
```

#### 访问网页
http://localhost:8000/

(备注：flask的app运行时，必须指定host='0.0.0.0',端口得通过EXPOSE指定，在程序中不指定)