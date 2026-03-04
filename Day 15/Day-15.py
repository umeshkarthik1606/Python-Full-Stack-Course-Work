'''
try:
    if a>10:
        print('good')

except NameError:
    print('a is not defined')
except ValueError:
    print('Enter the requested data type')
except TypeError:
    print('Data types are different')
except ZeroDivisionError:
    print('Can not divide with 0')
except IndexError:
    print('The index is not present')
except KeyError:
    print('In dict this key is not present')

else:
    print('No Error')
finally:
    print('End of the block')

try:
    a=a+'8'
    print(a[4])
except (NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError)as e:
    print(f'Error Occured: {e}')

else:
    print('No error')
finally:
    print('End of the block')

try:
    a=a+'8'
    print(a[4])
except Exception as e:
    print(f'Error Occured: {e}')

else:
    print('No error')
finally:
    print('End of the block')
'''
