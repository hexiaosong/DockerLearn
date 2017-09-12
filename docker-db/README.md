## Docker运行数据库

#### docker运行mysql数据库
1.拉取镜像
```
sudo docker pull mysql
```
2.运行镜像
```
sudo docker run --name first-mysql -p 3306:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql
# 挂在本地数据目录到容器目录
sudo docker run --name first-mysql -p 3306:3306 -v /Users/apple/Downloads/temp/docker-demo/docker-db/data:/var/lib/mysql -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql
#通过指定不同端口可运行多个mysql容器  宿主机连接使用端口3307
sudo docker run --name second-mysql -p 3307:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mysql
#进入运行中的mysql容器
docker exec -it first-mysql bash
#继续登录mysql
mysql -u root -p
```
3.navicat连接
```
host:localhost   #若是阿里云则为公网IP
password:123456
```

### docker运行mongodb数据库
1.拉取镜像
```
sudo docker pull mongo:3.0.2
```
2.运行镜像
```
docker run --name first-mongo -p 27017:27017 -v /Users/apple/Downloads/temp/docker-demo/docker-db/mongodb/data:/data/db -d mongo:3.0.2
```
3.mongochef连接
```
host:localhost
password:
```
4.docker运行mongodb镜像设置用户名密码验证
docker使用auth模式启动和mongodb使用auth模式启动类似，先创建用户再使用auth模式启动。因此首先不使用auth模式启动，创建后再以auth启动.
* 以普通模式启动
```
docker run --name first-mongo -p 27017:27017 -v /Users/apple/Downloads/temp/docker-demo/docker-db/mongodb/data:/data/db -d mongo:3.0.2
```
* 进入mongodb的客户端
```
docker run -it mongo:3.0.2 mongo --host 192.168.1.102
```
进入mongodb客户端后创建用户
```
use admin
#此时用户列表为空
db.system.users.find()
#创建管理员账户，比如，创建一个用户名为super, 密码为superpwd的管理员账户
db.createUser({
          user: 'super',
          pwd: 'superpwd',
          roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] });
#创建管理员后，需要给管理员授权，否则无权限操作用户
db.auth('super','superpwd')
#如果结果返回1，则表示授权成功，返回0则表示失败
```

至此，管理员账号创建完毕.再使用管理员账户创建普通用户,比如，现在我需要创建一个blog数据库，并且给这个数据库添加一个用户，用户名为develop,密码为developpwd.只有这个用户可以操作这个blog数据库.
重新以auth模式启动mongodb后进入mongodb客户端
```
docker run --name first-mongo -p 27017:27017 -v /Users/apple/Downloads/temp/docker-demo/docker-db/mongodb/data:/data/db -d mongo:3.0.2 --auth

docker run -it mongo:3.0.2 mongo --host 192.168.1.102
use admin
db.auth('super','superpwd')
show dbs

use blog
db.createUser({user: "develop",pwd: "developpwd",roles: [ { role: "readWrite", db: "blog" } ]})
db.auth('develop','developpwd')
至此，只能读写blog数据库的用户已创建完毕.
```

在admin数据库认证条件下的常用操作：
查看用户列表：db.system.users.find()
查看某个用户信息:db.runCommand({usersInfo:用户名})
修改用户信息:db.runCommand(
  {
    updateUser:用户名,
    pwd:密码,
    customData:{title:"xxx"……}
  }
)
修改用户密码:db.changeUserPassword(‘user’,’pwd’);
删除用户:db.system.users.remove({user:”username”});


(备注：
docker stop container_name/container_id
docker rm $(docker ps -a -q)
)

### docker运行redis数据库



```
sudo docker pull redis
```
2.运行镜像
```
docker run -p 6379:6379 --name first-redis -v /Users/apple/Downloads/temp/docker-demo/docker-db/redis/data:/data  -d redis redis-server --appendonly yes

#连接redis客户端查看
docker run -it redis redis-cli -h 192.168.1.102
```