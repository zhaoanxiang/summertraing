//#include<iostream>
//#include<fstream>
//#include<cstdlib>
//using namespace std;
//int main(){
//	ifstream inFile;
//	inFile.open("sum.txt");
//	if (!inFile.is_open()){
//		cout << "���ܴ��ļ�" << endl;
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
//		cout << "�ļ��Ѿ�����" << endl;
//	else if (inFile.fail())
//		cout << "�ļ���ȡʧ��" << endl;
//	else
//		cout << "������Ϊδ֪ԭ����ֹ"<<endl;
//	if (count == 0)
//		cout << "û�����ݴ���" << endl;
//	else{
//		cout << "�ܹ�" << count << "�����ݴ���" << endl;
//		cout << "�����ܺͣ�" << sum << endl;
//	}
//	system("pause");
//	return 0;
//	
//	}
