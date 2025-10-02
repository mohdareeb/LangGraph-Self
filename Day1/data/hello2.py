# print("hii")
# st="34"
# print(st)
# a=int(st)
# print(a)

# ans=""
# while a >0:
#     if a%2!=0:
#         ans=str(a)
#         break
#     else:
#         a=a//10

# print(ans)

st="234"

print(st)
print(st[-1:-2:-1])
while True:
    a=st[-1:-2:-1]
    n=int(a)
    if n%2!=0:
        print(a)
        break
    else:
        st=st[:-1]
        if len(st)==0:
            break
           