# C++中基类继承 enable_shared_from_this 之后派生类无法使用 shared_from_this() 的解决方法

在很多情况下，我们会在基类中继承 std::enable_shared_from_this 来使得在该类的方法中能够使用 shared_ptr 托管的 this 指针。但如果在子类中使用 shared_from_this() 函数，就会发生错误。

分析其原因，是因为 Base 在继承enable_shared_from_this<T>时，向模板T传递的类型为Base，也就是 shared_from_this() 函数返回值类型被设定为了 std::shared_ptr<Base>。所以在 子类中调用 shared_from_this()，返回值就是std::shared_ptr<Base>了。由于我们无法将裸指针或是智能指针从基类隐性转换至派生类，所以会发生错误。这时我们就需要显性的对返回值类型进行转换。

解决方法是使用std::dynamic_pointer_cast<子类>(shared_from_this())将返回的指针转换为派生类类型的指针：
最后需要注意两点： 

1. 使用std::dynamic_pointer_cast<T>()需要基类中存在虚函数，<font color='red'>这是由于这个转换函数使用输入的类型和目标类型中是否存在相同签名的虚函数作为转换能否成功的标识</font> 。最简单也是正确的解决方法是将基类中的析构函数声明为虚函数。 
2. 不能在构造函数中使用shared_form_this()。这是由于std::enable_share_from_this在实现时使用了一个对象的weak_ptr，而这个weak_ptr需要对象的shared_ptr进行初始化。由于此时对象尚未构造完成，所以会抛出std::bad_weak_ptr的异常。关于这点目前没有较为完美的方案，可以尝试写一个init()函数，在对象构造后手动调用。或是手动写一个std::shared_ptr<Derived>(this)使用，但这种解决方案可能造成循环引用。更多方案请查阅StackOverFlow。
