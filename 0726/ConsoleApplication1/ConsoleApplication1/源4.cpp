//#include<iostream>
//#include<fstream>
//using namespace std;
//int main(){
//	ofstream ofs;
//	char filename[16] = "write.txt";
//	int a = 1;
//	ofs.open(filename, ios::out);
//	for (int i=1; i < 4; i++)
//		ofs << i << "" << endl;
//		ofs.close();
//		ofs.clear();
//		ifstream inFile;
//
//			inFile.open("write.txt");
//			if (!inFile.is_open()){
//				cout << "不能打开文件" << endl;
//				exit(EXIT_FAILURE);
//			}
//			double value;
//			double sum = 0;
//			int count = 0;
//			inFile >> value;
//			while (inFile.good()){
//				++count;
//				sum += value;
//				inFile >> value;
//			}
//			if (inFile.eof())
//				cout << "文件已经读完" << endl;
//			else if (inFile.fail())
//				cout << "文件读取失败" << endl;
//			else
//				cout << "输入因为未知原因终止"<<endl;
//			if (count == 0)
//				cout << "没有数据处理" << endl;
//			else{
//				cout << "总共" << count << "个数据处理" << endl;
//				cout << "数据总和：" << sum << endl;
//			}
//			
//
//system("pause");
//return 0;
//}