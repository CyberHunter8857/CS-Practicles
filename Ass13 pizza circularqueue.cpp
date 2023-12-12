
#include<iostream>
#define MAX 5
using namespace std;

class cqueuepizza
{
public:
	int q[MAX],rear,front;
	cqueuepizza();
	void insert(int);
	void delete1();
	void display();
};

cqueuepizza :: cqueuepizza()
{
	front=rear=-1;
}
void cqueuepizza::insert (int value)
{
	if ((rear+1)%MAX==front){
		cout<<"\n Queue is Full";
    }
	else if(front==-1 && rear==-1)
	{
		front=rear=0;
        q[rear]=value;
	}
    else{
        rear=(rear+1)%MAX;
        q[rear]=value;
    }
}

void cqueuepizza::delete1 ( )
{
    if(front==-1 && rear==-1){
        cout<<"empty";
        return;
    }
    else if(front==rear){
        cout<<"Dleleted ele is"<<q[front];
        front=rear=-1;

    }
    else{
        cout<<"Deleted ele is"<<q[front];
        front=(front+1)%MAX;
    }
}

void cqueuepizza :: display()
{
	int i=front;

	cout<<endl;
    if(front==-1 && rear==-1){
        cout<<"empty"<<endl;
        return;
    }
    else{
        while(i!=rear){
            cout<<" "<<q[i];
            i=(i+1)%MAX;
        }
        cout<<" "<<q[rear];
    }
}
int main()
{
	int choice,x,y;
	char ans;
	cqueuepizza q1;
	do
	{

		cout<<"\n*****MENU*****";
		cout<<"\n1. Place an order id ";
		cout<<"\n2. Remove an order id ";
		cout<<"\n3. Display the queue ";
		cout<<"\nEnter your choice: ";
		cin>>choice;
		switch(choice)
		{
		case 1: cout<<"\n Enter the order id  :  ";
				cin>>y;
				q1.insert(y);
				q1.display();
				break;
		case 2:  q1.delete1();
				 q1.display();
				 break;
		case 3:  q1.display();
				 break;
		default: cout<<"\nWrong choice!!";
				 break;
		}
		cout<<"\nDo you want to continue(y/n)??";
		cin>>ans;
	}while(ans=='y');
	return 0;
}