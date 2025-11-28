class multipleFunctions():
    def Subfields():
        my_list=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for each_subfield in my_list:
            print(each_subfield)


    def OddEven():
        number=int(input("Enter a number: "))
        if number%2==0:
            print(f"{number} is  Even number")
        else:
            print(f"{number} is  Odd number")


    def Eligible(Gender,Age):
        print(f"Your Gender: {Gender}")
        print(f"Your Age: {Age}")
        if (Gender=="MALE" and Age>=21) or (Gender=='FEMALE' and Age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")


    def percentage():
        Subject1=int(input("Subject1= "))
        Subject2=int(input("Subject2= "))
        Subject3=int(input("Subject3= "))
        Subject4=int(input("Subject4= "))
        Subject5=int(input("Subject5= "))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Full_marks=500
        percent=(Total/Full_marks)*100
        print(f"Total : {Total}")
        print(f"Percentage : {percent}")

    def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print(f"Area of Triangle: {(Height*Breadth)/2}")
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print(f"Perimeter of Triangle: {Height1+Height2+Breadth}")