import Fraction

def main():

    myfraction = Fraction.Fraction()

    #Determine if 3/9 is reduceable
    myfraction.Numerator = 3
    myfraction.Denominator = 9

    Isreduceable = myfraction.Reducible()

    if myfraction.Reducible():
        print('The fraction is reduceable.')
    else:
        print('The fraction isn\'t reduceable.')


    #Display the float equivalent of 3/4
    myfraction.Numerator = 3
    myfraction.Denominator = 4

    print('This is the fraction in float form:', myfraction.ToFloat())
    

    #Display the most reduced form of 15/45
    myfraction.Numerator = 15
    myfraction.Denominator = 45

    print('The reduced form is:', myfraction.Reduce())


    #Display the result of 1/2+1/4
    myfraction.Numerator = 1
    myfraction.Denominator = 2

    new = Fraction.Fraction()
    new.Numerator = 1
    new.Denominator = 4

    print('The sum of the fractions is', new.Add(myfraction))


    #Determine if 7/9 is < > or == 4/5
    myfraction.Numerator = 7
    myfraction.Denominator = 9

    new.Numerator = 4
    new.Denominator = 5

    comparethem = myfraction.CompareToMe(new)

    if comparethem == -1:
        print('the first fraction is smaller')
    elif comparethem == 1:
        print('the first fraction is larger')
    else:
        print('the fractions are equal.')
        

    #Display the float equivalent of 1/5+1/4
    myfraction.Numerator = 1
    myfraction.Denominator = 5

    new.Numerator = 1
    new.Denominator = 4

    print('The float form of the sum is', (myfraction.ToFloat() + new.ToFloat()))
        

    #Determine if 2/3 is equal to 6/9
    myfraction.Numerator = 2
    myfraction.Denominator = 3

    new.Numerator = 6
    new.Denominator = 9

    comparethem = myfraction.CompareToMe(new)

    if comparethem == 0:
        print('these fractions are equivalent')
    else:
        print('the fractions are not equal.')


    #Determine if (1/2+1/4 ) = 6/8
    myfraction.Numerator = 1
    myfraction.Denominator = 2

    new = Fraction.Fraction()
    new.Numerator = 1
    new.Denominator = 4

    new = new.Add(myfraction)

    myfraction.Numerator = 6
    myfraction.Denominator = 8

    comparethem = myfraction.CompareToMe(new)

    if comparethem == 0:
        print('the sum of these fractions = 6/8')
    else:
        print('the sum is not 6/8')


    #Display the most reduced form of 6/8
    myfraction.Numerator = 6
    myfraction.Denominator = 8

    print('The reduced form is:', myfraction.Reduce())

main()
