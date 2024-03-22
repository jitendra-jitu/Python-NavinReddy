""" def jitu():
    yield 1
    yield 2
    yield 3
j=jitu()
k=jitu() """

# def fib(l):
#     a,b=0,1
#     for i in range(l):
#         yield a
#         a,b=b,a+b
# f1=fib(8)
# for i in f1:
#     print(i)

# generator expression
exp=(0 for i in  range(5) if i==0 or i== 1)

for i in exp:
    print(i)
