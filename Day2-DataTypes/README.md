This lesson is meant to explain the different data types in python
like str, int, float, bool and how to manipulate them. Data types can be combined
into varible but they need to be the same type. A str and an int
cannot combine. However, we can change a str to an int with:
    
    int(str)

And visa versa.

    str(int)

This simple BMI calculator is meant to show how to convert str to diff numerical types
like int and float:  

    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    
    #Write your code below this line 👇
    
    bmi = int(weight) / float(height) ** 2
    bmi_as_int = int(bmi)
    print(bmi_as_int)

In today's final project, we work with many data types along the way
and have to convert them into diff types to be able to work together
and with certain functions. in addition, we used the round function and an F-string
to manipulate data into a presentable fashion. 
