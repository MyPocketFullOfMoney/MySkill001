# 前言

该模块中主要记录工作中遇到与MySql有关的问题  

## 常用指令  

- 显示表结构  
    `desc [tablename]`  
- 查看建表语句  
    `show create table [tablename]`

## 常用函数

### concat

### sum

### date_format

### sysdate

### ifnull

### 开窗函数

## MySQL存储引擎

### InnoDB

### MyISAM

## 事务

事务的特性：ACID。原子性、一致性、隔离性、持久性

## 索引的原理

## 主键和外键

主键定义：表中经常有一列或多列的组合，其值能唯一的标识表中的每一行。

## 数据库锁的分类

按锁的粒度划分：行级锁、页级锁、表级锁
按使用方式划分：悲观锁、乐观锁
