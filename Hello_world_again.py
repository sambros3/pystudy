languages = ['python', 'perl', 'c', 'java']

# for lang in languages:
#     if lang in ['python', 'perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in ['c', 'java']:
#         print("%6s need compiler" % lang)
#     else:
#         print("should not reach here")


print("=" * 50)
print("I'm studing how to programming python!")
print("=" * 50)

multiline='''
    Life is too short
    You need python
    '''
print(multiline)
print("Length of multiline : %d" % len(multiline) )

a = "Pithon"
a = a[:1]+'y'+a[2:]
# a[1] = "y"
print (a)










i = 0
# for i in [0,2,3]:
def add(i):
    i=i+1
    return i


while i<3:
    i = add(i)
    print(i)