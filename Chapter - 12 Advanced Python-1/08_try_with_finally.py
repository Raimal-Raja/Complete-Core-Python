def main():
    try: 
        a = int(input("Enter number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    
    # print("this will not run if above any passed")
    
    finally:
        print('Hey i am inside finally')
        
m = main()