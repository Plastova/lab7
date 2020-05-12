#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

double h=0.8, eps0=0.01;
double A[2][2]={{0,-1},{0.8,1.6}};
double y_pr[2]={1,0}, y_res[2]={1,0}, phi[2]={0,0};
double x=0, eps1,eps2,temp;
double sum1=0,sum11=0,sum2=0,sum22=0;

int iter=0;

void Euler(double h){
	y_pr[1]+=h*(phi[1]-A[1][1]*y_pr[1]-A[1][0]*y_pr[0]);
	y_pr[0]+=h*y_pr[1];	
}

void simmetr(double h){	
	y_res[1]+=(h*phi[1]-0.5 * A[1][0]*h*(y_pr[0]+y_res[0])-0.5*A[1][1]*h*(y_pr[1]+y_res[1]));
	y_res[0]+=h*(-0.5*(A[0][0]*(y_pr[0]+y_res[0])+A[0][1]*(y_pr[1]+y_res[1])));
	}
	
void make_values(double h, ofstream& fout){
	
	fout.open("result.txt",ios_base::app); 
    fout<<x<<" "<<y_res[0]<<" "<<y_res[1]<<endl;
	while(x<2){
	iter++;
	x+=h;
	phi[1]=x*exp(-x)/5;
	Euler(h);
	simmetr(h);
	fout<<x<<" "<<y_res[0]<<" "<<y_res[1]<<endl;
	y_pr[0]=y_res[0];
	y_pr[1]=y_res[1];	
}
	fout.close();	
}

void make_sum(ofstream& fout,ifstream& fin) {	
	make_values(h,fout);
	fin.open("result.txt");
		if(fin){		
			fin>>temp;
			fin>>temp;
			sum1+=temp;
			fin>>temp;
			sum11+=temp;
		}
		fin.close();
		
		fout.open("result.txt",ios_base::trunc);
		fout.close();		
		x=0;
		y_pr[0]=1;
		y_pr[1]=0;
		y_res[0]=1;
		y_res[1]=0;
			
		make_values(h/2,fout);
		fin.open("result.txt",ios_base::in);
		if(fin){
			fin>>temp;
			fin>>temp;
			fin>>temp;
			
			fin>>temp;
			fin>>temp;
			sum2+=temp;
			fin>>temp;
			sum22+=temp;
		}
			fin.close();
		eps1 = abs(sum2-sum1);
		eps2 = abs(sum22-sum11);
}

void Runge(ofstream& fout,ifstream& fin) {
	make_sum(fout,fin);
	int it=0;
	while ((eps1 >=eps0)||(eps2>=eps0)) {
	it++;
	h /=2 ;	
	fout.open("result.txt",ios_base::trunc);
	fout.close();
	sum1=0;
	sum2=0;
	sum11=0;
	sum22=0;
	x=0;
	y_pr[0]=1;
	y_pr[1]=0;
	y_res[0]=1;
	y_res[1]=0;
	
	make_sum(fout,fin);
}
	cout<<"\neps1 (dlya y)="<<eps1<<"\neps2 (dlya y')="<<eps2<<endl;
	cout<<"h="<<h;
	cout<<" - naiden po pravilu Runge. Kolichestvo iteratsiy: "<<it<<endl;
	fout.open("result.txt",ios_base::trunc);
	fout.close();
}


int main() {	
	ofstream fout;
	ifstream fin;
	Runge(fout,fin);
	x=0;
	y_pr[0]=1;
	y_pr[1]=0;
	y_res[0]=1;
	y_res[1]=0;
	iter=0;
	make_values(h,fout);
	cout<<"\n\nZnacheniya zapisany. Kolichestvo tochek: "<<iter<<endl;
	return 0;
}
