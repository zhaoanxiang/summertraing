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
//				cout << "���ܴ��ļ�" << endl;
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
//				cout << "�ļ��Ѿ�����" << endl;
//			else if (inFile.fail())
//				cout << "�ļ���ȡʧ��" << endl;
//			else
//				cout << "������Ϊδ֪ԭ����ֹ"<<endl;
//			if (count == 0)
//				cout << "û�����ݴ���" << endl;
//			else{
//				cout << "�ܹ�" << count << "�����ݴ���" << endl;
//				cout << "�����ܺͣ�" << sum << endl;
//			}
//			
//
//system("pause");
//return 0;
//}