#include <iostream>
using namespace std;

/*
* 字符串对象的操作
*/

// 函数声明
int ReadString();
int GetlineString();

int main()
{
    string s1, s2;
    cin >> s1 >> s2;          // 把第一个输入读到s1中，第二个输入读到s2中
    cout << s1 << s2 << endl; // 输出两个string对象
    ReadString();
    GetlineString();
    return 0;
}

int ReadString()
{
    string word;
    cout << "cin 00 exit ReadString() function!!!" << endl;
    while (cin >> word){
        cout << word << endl;
        if ("00" == word){
            break;
        }
    }
    return 0;
}

int GetlineString()
{
    cout << "This is GetlineString() function!!!" << endl;
    string line;
    // 每次读入一整行，直至到达文件尾。字符串对象line不存储换行符。
    while (getline(cin, line))
        cout << line << endl;
    return 0;
}