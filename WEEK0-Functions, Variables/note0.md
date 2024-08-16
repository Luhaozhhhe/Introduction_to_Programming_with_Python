# WEEK0-Functions, Variables

想输出`print("hello,"friend"")`，这样会引起歧义

我们需要使用`print("hello, \"friend\"")`



```python
name = input("What's your name? ")
print(f"hello, {name}")
```

我们使用f来输出我们的原文hello

这个f是一个特殊的指示符，Python用一种特殊的方式来处理这个字符串



```python
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")
```

此处的strip用于去除我们想要去除的东西



```python
name = name.title()
```

title用于把第一个字母大写



```python
name = name.strip().title()
```

这就是先去除空格，然后把第一个字母大写



```
z = round(x / y, 2)

print(f"{z:.2f}")
```

将z保留两位小数





