def generate_fibonacci_sequence(NUM):                                           # Generating fibonacci series of NUM number of terms
    List_Fib = []                                                               # Initialize an array to store the fibonacci series
    List_Fib.append(0)                                                          # Append 0 to 1 to this array to start the series
    List_Fib.append(1)
    while (len(List_Fib) <= NUM):                                               # The condition for this while loop is to check if the length has reched NUM number of terms
        Last = List_Fib[-1]                                                     # We keep retrieving the last two terms in the sries 
        Second_Last = List_Fib[-2]  
        List_Fib.append(Last+Second_Last)                                       # Append the sum of these terms to the end of the series
    return(List_Fib)

def is_prime(number):                                                           # This function takes a number as parameter and return True or False whether is prime or not
    if (number == 1):                                                           # Write a case for "1" since its not prime
        return(False)
    for  i in range (2,number):                                                 # We iterate from 2 till that number to check if the number is divisible 
        if (number % i == 0):
            return (False)
    return (True)
        
def customize_fib(LIST):                                                        # We give our Fibonacci series as input and convert each element to Buzz, Fizz , BuzzFizz, etc based on the condition
    ANSWER = []                                                                 # We intialise a list called ANSWER where we store our customized Fibonacci series
    for i in range (0,len(LIST)):                                               # loop to iterate over all the elements in Fib_Seq list
        ELEMENT = LIST[i]                                                       # Each element from Fib_Seq list is checked with the conditions
        if (ELEMENT == 0):                                                      # If the element is zero we just append into ANSWER list
            ANSWER.append(ELEMENT)
            continue
        if ((ELEMENT % 3 == 0) and not (ELEMENT % 5 == 0)):                     # check for divisibility by 3
            ANSWER.append("Buzz")
            continue
        elif ((ELEMENT % 5 == 0) and not (ELEMENT % 3 == 0)):                   # check for divisibility by 5
            ANSWER.append("Fizz")
            continue           
        elif ((ELEMENT % 3 == 0) and (ELEMENT % 5 == 0)):                       # check for divisibility by 3 and 5 (15)
            ANSWER.append("FizzBuzz")
            continue
        BOOL = is_prime(ELEMENT)                                                # check if element is prime by calling is_prime function
        if (BOOL == True):
            ANSWER.append("BuzzFizz")
        elif (BOOL == False):
            ANSWER.append(ELEMENT)                                              # After all conditions are checked and if element doesnot satisfy any condition then append element 
    return(ANSWER)
            
    
if __name__ == "__main__":                                                      # Main function
    n = int(input())                                                            # n is the number of elements in series
    Fib_Seq = generate_fibonacci_sequence(n)                                    # Give n as the input to this function and generate our fibonacci serier with length n
    print(Fib_Seq)                                                              # The original fibonacci series
    Customized_Fib_Seq = customize_fib(Fib_Seq)                                 # Give our fibonacci series as input to customize_fib function to modify it to add Fizz, Buzz, etc.
    print (Customized_Fib_Seq)                                                  # This is our final solution
    
