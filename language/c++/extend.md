1、virtual 继承时

```
class A
{
    public :
    int dataA;
}

class B: virtual public A
{
    public :
    int dataB;
}
```
说明：
sizeof(B) 大小为12，  

    int dataA -> 4

    int dataB -> 4 

    virtp     -> 4

```
class B: public A
{
    public :
    int dataB;
}
```

sizeof(B)  -> 8 int dataA int dataB

```
class C:virtual public A
{
    public :
    int dataC;
}

class D:public B, public C
{
    public :
    int dataD;
}
```

如果没有虚继承：
siezof(D) 20  int data B(A,B) C(A,C) D

如果有虚继承：
sizeof(D)24  
vbptr：继承自父类B中的指针
int dataB：继承自父类B的成员变量
vbptr：继承自父类C的指针
int dataC：继承自父类C的成员变量
int dataD：D自己的成员变量
int A：继承自父类A的成员变量