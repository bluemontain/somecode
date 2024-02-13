#!/usr/bin/python3
#coding:utf-8
import os
import readline
def get_tomcat(): #获取tomcat服务的函数
    tomcat_port = os.popen("netstat -anput |grep 38080 | grep LISTEN | awk '{print $4}' | awk -F: '{print $4}'")
    tomcat_port = tomcat_port.read().strip()
    return tomcat_port
def get_nginx():#获取nginx服务的函数
    nginx = os.popen("ps -aux | grep -v grep | grep nginx | grep master | awk '{print $12}'")
    nginx = nginx.read().strip()
    return nginx
def get_nginx_port():#获取nginx端口的函数
    nginx_port = os.popen("netstat -anput |grep -v grep | grep LISTEN | grep nginx | awk '{print $4}' | awk -F: '{print $2}'| tr '\n' ' '")
    nginx_port = nginx_port.read().strip()
    return nginx_port
def get_redis():#获取redis服务的函数
    redis = os.popen("netstat -anput |grep redis | grep LISTEN | awk '{print $4}' | awk -F: '{print $2}'")
    redis = redis.read().strip()
    return redis
def get_mysql():#获取mysql服务的函数
    mysql = os.popen("netstat -anput | grep mysql | grep LISTEN | awk '{print $4}' | awk -F: '{print $4}'")
    mysql = mysql.read().strip()
    return mysql
def get_mq():#获取apache-mq服务的函数
    mq = os.popen("netstat -anput |grep 61616 | grep LISTEN | awk '{print $4}' | awk -F: '{print $4}'")
    mq = mq.read().strip()
    return mq
def get_fdfs_trackerd():#获取FastDFS-tracker服务的函数
    trackerd = os.popen("netstat -anput |grep fdfs | grep LISTEN | grep trackerd  | awk '{print $4}' | awk -F: '{print $2}'")
    trackerd = trackerd.read().strip()
    return trackerd
def get_fdfs_storaged():#获取FastDFS-storage服务的函数
    storaged = os.popen("netstat -anput |grep fdfs | grep LISTEN | grep storaged  | awk '{print $4}' | awk -F: '{print $2}'")
    storaged = storaged.read().strip()
    return storaged
def get_openfire():#获取openfire服务的函数
    openfire = os.popen("netstat -anput |  grep 9090 | grep LISTEN | awk '{print $4}' | awk -F: '{print $4}'")
    openfire = openfire.read().strip()
    return openfire
def get_es():#获取elasticsearch服务的函数
    es = os.popen("ps -aux |grep -v grep |grep elasticsearch")
    es = es.read().strip()
    return es
def all_service():#调用所有以上编写函数的方法
        if get_tomcat() == '38080':
            print('>>>Tomcat 服务运行正常！ 端口：38080')
        else:
            print('>>>ERROR<<<: Tomcat服务可能不存在或已宕机，请立即检查！')
        if get_nginx() == 'master':
            print('>>> Nginx 服务运行正常！端口：' + get_nginx_port())
        else:
            print('>>>ERROR<<<: Nginx 服务可能不存在或已宕机，请立即检查！')
        if get_redis() != '':
            print('>>> Redis 服务运行正常！ 端口：' + get_redis())
        else:
            print('>>>ERROR<<<: Redis 服务可能不存在或已宕机，请立即检查！')
        if get_mysql() != '':
            print('>>> Mysql 服务运行正常！ 端口：' + get_mysql())
        else:
            print('>>>ERROR<<<: Mysql 服务可能不存在或已宕机，请立即检查')
        if get_mq() != '':
            print('>>> apache-MQ服务运行正常！ 端口：' + get_mq())
        else:
            print('>>>ERROR<<: apache-MQ服务可能不存在或已宕机，请立即检查！')
        if get_fdfs_trackerd() and get_fdfs_storaged() != '':
            print('>>> FastDFS服务运行正常！ tracker端口：' + get_fdfs_trackerd() + ' ' + 'storage端口：' + get_fdfs_storaged())
        elif get_fdfs_trackerd() == '':
            print('>>>ERROR<<: FastDFS服务运行异常，未监听到trackerd端口，storage端口：' + get_fdfs_storaged())
        elif get_fdfs_storaged() == '':
            print('>>>ERROR<<: FastDFS服务运行异常，未监听到storage端口，tracker端口：' + get_fdfs_trackerd())
        else:
            print('>>>ERROR<<<: FastDFS服务可能不存在或已宕机，请立即检查！')
        if get_openfire() != '':
            print('>>> Openfire服务运行正常！ 端口：' + get_openfire())
        else:
            print('>>>ERROR<<<: Openfire服务可能不存在或已宕机，请立即检查！')
        if get_es() != '':
            print('>>> elasticsearch服务运行正常！端口未知！请手动查看！')
        else:
            print('>>>ERROR<<<: elasticsearch服务可能不存在或已宕机，请立即检查！')
def get_service():#调用单个服务函数的方法
    try: #在用户输入当中可能会发生的异常处理
        service = input("===输入服务名查看状态（all：查看全部服务状态）：").lower()
        if service == 'tomcat':
            if get_tomcat() == '38080':
                print('>>>Tomcat 服务运行正常！ 端口：38080')
            else:
                print('>>>ERROR<<<: Tomcat服务可能不存在或已宕机，请立即检查！')
        elif service == 'nginx':
            if get_nginx() == 'master':
               print('>>> Nginx 服务运行正常！端口：' + get_nginx_port())
            else:
                print('>>>ERROR<<<: Nginx 服务可能不存在或已宕机，请立即检查！')
        elif service == 'redis':
            if get_redis() != '':
                print('>>> Redis 服务运行正常！ 端口：' + get_redis())
            else:
                print('>>>ERROR<<<: Redis 服务可能不存在或已宕机，请立即检查！')
        elif service == 'mysql':
            if get_mysql() != '':
                print('>>> Mysql 服务运行正常！ 端口：' + get_mysql())
            else:
                print('>>>ERROR<<<: Mysql 服务可能不存在或已宕机，请立即检查')
        elif service == 'mq':
            if get_mq() != '':
                print('>>> apache-MQ服务运行正常！ 端口：' + get_mq())
            else:
                print('>>>ERROR<<: apache-MQ服务可能不存在或已宕机，请立即检查！')
        elif service == 'fdfs' or service == 'fastdfs':
            if get_fdfs_trackerd() and get_fdfs_storaged() != '':
                print('>>> FastDFS服务运行正常！ tracker端口：' + get_fdfs_trackerd() + ' ' + 'storage端口：' + get_fdfs_storaged())
            elif get_fdfs_trackerd() == '':
                print('>>>ERROR<<: FastDFS服务运行异常，未监听到trackerd端口，storage端口：' + get_fdfs_storaged())
            elif get_fdfs_storaged() == '':
                print('>>>ERROR<<: FastDFS服务运行异常，未监听到storage端口，tracker端口：' + get_fdfs_trackerd())
            else:
                print('>>>ERROR<<<: FastDFS服务可能不存在或已宕机，请立即检查！')
        elif service == 'openfire':
            if get_openfire() != '':
                print('>>> Openfire服务运行正常！ 端口：' + get_openfire())
            else:
                print('>>>ERROR<<<: Openfire服务可能不存在或已宕机，请立即检查！')
        elif service == 'es' or service == 'elasticsearch':
            if get_es() != '':
                print('>>> elasticsearch服务运行正常！端口未知！请手动查看！')
            else:
                print('>>>ERROR<<<: elasticsearch服务可能不存在或已宕机，请立即检查！')
        elif service == 'all':
            all_service()
        else:
            print('[ERROR]:您可能输入了一个错误的服务名！！！(进程已退出)')
 
    except KeyboardInterrupt:
        print('用户已暴力结束进程，输入中断！')
try: #判断获取函数方法调用是否有异常
    get_service()
except Exception as e:
    print('[ERROR]:执行错误：调用 “get_service()” 函数失败！')