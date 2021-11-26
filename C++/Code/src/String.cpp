#include <iostream>
#include <string>
using std::string;
/*
* 字符串的定义
*/

string s1;          // 默认初始化，s1是一个空的字符串
string s2 = s1;     // s2是s1的副本
string s3 = "hiya"; // s3是该字符串面值的副本
string s4(10, 'c'); // s4的内容是cccccccccc

string s5 = "hiya"; // 拷貝初始化
string s6("hiya");  // 直接初始化
string s7(10, 'c'); //直接初始化，s7的内存是cccccccccc