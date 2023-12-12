#include<iostream>
using namespace std;
#define size 5
class dequeue{
    int a[10],front,rear,count;
    public:
    dequeue();
    void addbeg(int);
    void addend(int);
    void deltbeg();
    void deltend();
    void display();
};

dequeue::dequeue(){
    front=-1;
    rear=-1;
    count=0;
}

void dequeue::addbeg(int x){
    int i;
    if(front==-1){
        front++;
        rear++;
        a[rear]=x;
        count++;
    }
    else if(rear>=size-1){
        cout<<"overflow"<<endl;
        return;
    }
    else{
        for(i=count;i>=0;i--){
            a[i]=a[i-1];
        }
        a[i]=x;
        count++;
        rear++;
    }
}

void dequeue::addend(int x){
    if(front==-1){
        front++;
        rear++;
        a[rear]=x;
        count++;
    }
    else if(rear>=size-1){
        cout<<"overflow"<<endl;
        return;
    }
    else{
        a[++rear]=x;
    }
}

void dequeue::deltbeg(){
    if(front==-1){
        cout<<"underflow"<<endl;
    }
    else{
        if(front==rear){
            front=rear=-1;
            return;
        }
        cout<<"Deleted ELE is:"<<a[front];
        front+=1;
    }
}

void dequeue::deltend(){
    if(front==-1){
        cout<<"underflow"<<endl;
        return;
    }
    else{
        if(front==rear){
            front=rear=-1;
            return;
        }
        cout<<"Deleted ELE is:"<<a[rear];
        rear=rear-1;
    }
}

void dequeue::display(){
    for(int i=front;i<=rear;i++){
        cout<<a[i]<<" ";
    }
}

int main(){
    int x,ch;
    dequeue d;
    do{
        cout<<"Menu: 1.Addbeg 2.Addend 3.deltbeg 4.deltend 5.display";
        cin>>ch;
        switch (ch)
        {
        case 1:
            cout<<"Enter ele"<<endl;
            cin>>x;
            d.addbeg(x);
            break;
        case 2:
            cout<<"Enter ele"<<endl;
            cin>>x;
            d.addend(x);
            break;
        case 3:
            d.deltbeg();
            break;
        case 4:
            d.deltend();
            break;
        case 5:
            d.display();
            break;
        default:
            cout<<"Invalid choice";
            break;
        }
    }while(ch!=7);
    return 0;
}