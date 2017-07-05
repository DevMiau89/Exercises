def func(*args, **kwargs):
    for arg in args:
        print arg
    for item in kwargs.items():
        print item

func(x=456, y=3)


print 'First module name is {}'. format(__name__)
print('This text about CodeCouple blog will be always printed')

if __name__ == '__main__':
    print('Run directly')
else:
    print('Run from import')
