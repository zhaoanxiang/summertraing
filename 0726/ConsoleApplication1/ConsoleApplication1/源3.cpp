//#include<iostream>
//#include<fstream>
//#include<cstdlib>
//using namespace std;
//int main(){
//	ifstream inFile;
//	inFile.open("sum.txt");
//	if (!inFile.is_open()){
//		cout << "不能打开文件" << endl;
//		exit(EXIT_FAILURE);
//	}
//	double value;
//	double sum = 0;
//	int count = 0;
//	inFile >> value;
//	while (inFile.good()){
//		++count;
//		sum += value;
//		inFile >> value;
//	}
//	if (inFile.eof())
//		cout << "文件已经读完" << endl;
//	else if (inFile.fail())
//		cout << "文件读取失败" << endl;
//	else
//		cout << "输入因为未知原因终止"<<endl;
//	if (count == 0)
//		cout << "没有数据处理" << endl;
//	else{
//		cout << "总共" << count << "个数据处理" << endl;
//		cout << "数据总和：" << sum << endl;
//	}
//	system("pause");
//	return 0;
//	
//	}
