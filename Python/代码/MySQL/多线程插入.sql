show create table test_li.user;

select count(*) from test_li.user order by username;

insert into test_li.user (username,email,password,create_time) values ('xiaoming','123456@qq.com','123456',sysdate());

alter table test_li.user modify username bigint;

delete from test_li.user;