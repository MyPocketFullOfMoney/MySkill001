#include <iostream>
using namespace std;

/*
* 字符串对象的操作
*/

// 函数声明
int ReadString();
int GetlineString();
int ForString();

int main()
{
    string s1, s2;
    cin >> s1 >> s2;          // 把第一个输入读到s1中，第二个输入读到s2中
    cout << s1 << s2 << endl; // 输出两个string对象
    ReadString();
    GetlineString();
    ForString();
    return 0;
}

int ReadString()
{
    string word;
    cout << "cin 00 exit ReadString() function!!!" << endl;
    while (cin >> word)
    {
        cout << word << endl;
        if ("00" == word)
        {
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
    {
        cout << line << endl;
        if ("00" == line)
        {
            break;
        }
    }
    return 0;
}

int ForString()
{
    cout << "This is ForString() function." << endl;
    string s("Hello World!!!");
    // 抓换成大写形式
    for (auto &c : s)   // 对于s中的每个字符（注意：c是引用）
        c = toupper(c); // c是一个引用，因此赋值语句将改变s中字符的值
    cout << s << endl;
    return 0;
}