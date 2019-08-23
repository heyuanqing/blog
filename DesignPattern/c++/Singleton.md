```Singleton* getInstance()
{
    if (instance == NULL)
    {
	lock();
    	if (instance == NULL)
    	{
       		instance = new Singleton();
    	}
    	unlock();
    }

    return instance;
}
```

