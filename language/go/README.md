

1、反射后的对象，遍历成员时，只会编译一层不会递归遍历

```go
type Brand struct{
name string
length int
}
type FakeBrand = Brand

type Vehicle struct{
 FakeBrand
 Brand
}
var a Vehicle
// 取a的类型反射对象
	ta := reflect.TypeOf(a)

	// 遍历a的所有成员
	for i := 0; i < ta.NumField(); i++ {

		// a的成员信息
		f := ta.Field(i)

		// 打印成员的字段名和类型
		fmt.Printf("FieldName: %v, FieldType: %v\n", f.Name, f.Type.Name())
	}

输出为：
FieldName: FakeBrand, FieldType: Brand
FieldName: Brand, FieldType: Brand

```

```go
type Brand struct {
	nane string
	length int
}

type test struct{
	width int
	height int
}

// 为商标结构添加Show方法
func (t Brand) Show() {
}

// 为Brand定义一个别名FakeBrand
type FakeBrand = Brand

// 定义车辆结构
type Vehicle struct {

	// 嵌入两个结构
	FakeBrand
	Brand
	test
}

// 声明a变量为车辆类型
	var a Vehicle

	// 指定调用FakeBrand的Show
	a.FakeBrand.Show()

	// 取a的类型反射对象
	ta := reflect.TypeOf(a)

	// 遍历a的所有成员
	for i := 0; i < ta.NumField(); i++ {

		// a的成员信息
		f := ta.Field(i)

		// 打印成员的字段名和类型
		fmt.Printf("FieldName: %v, FieldType: %v \n", f.Name, f.Type.Name())
	}
输出为：
FieldName: FakeBrand, FieldType: Brand
FieldName: Brand, FieldType: Brand
FieldName: test, FieldType: test


```

遍历map

```go
	scene.Range(func(k, v interface{}) bool {

		fmt.Println("iterate:", k, v)
		return false
	})

return false 支持退出  return true 继续执行
```

变长参数

```go
func rawPrint(rawList ...interface{}) {

	// 遍历可变参数切片
	for _, a := range rawList {

		// 打印参数
		fmt.Println(a)
	}
}

	rawPrint(1, 2, 3)	
```

