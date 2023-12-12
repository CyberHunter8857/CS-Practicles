#include<iostream>
using namespace std;
#define size 5

class job{
    public:
    int a[size],front,rear;
    job(){
        rear=-1;
        front=-1;
    }
    void addjob(int);
    int deletejob();
    int isfull();
    int isempty();
    void display();
};

int job::isfull(){
    if(rear==size-1)
        return 1;
    else 
        return 0;
}

int job::isempty(){
    if(front==-1)
        return 1;
    else
        return 0;
}

void job::addjob(int x){
    if(isfull()==1){
        cout<<"Queue is full"<<endl;
    }
    else{
        rear++;
        a[rear]=x;
    }
}

int job::deletejob(){
    int value;
    if(isempty()==0){
        cout<<"Queue is empty"<<endl;
        return -999;
    }
    else{
        front++;
        value=a[front];
        return value;
    }
}

void job::display(){
    cout<<"The Queue is :"<<endl;
    for(int i=front+1;i<=rear;i++){
        cout<<" "<<a[i];
    }
}

int main(){
    int ch,x,y;
    char ans;
    job q;
    do{
        cout<<"Menu : 1.add 2.delete 3.display"<<endl;
        cin>>ch;
        switch (ch)
        {
        case 1:
            cout<<"Enter job"<<endl;
            cin>>x;
            q.addjob(x);
            q.display();
            break;
        case 2:
            y=q.deletejob();
            if(y!= -999)
            cout<<"Deleted Ele is:"<<y<<endl;
            q.display();
            break;
        case 3:
            q.display();
            break;
        default: 
            cout<<"wrong choice"<<endl;
            break;
        }
        cout<<"\ndo you want to continue(y/n)"<<endl;
        cin>>ans;
    }while(ans=='y');
    return 0;
}