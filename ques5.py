l=24
list=[113,175,12]
def main(a,l=24):
    print("class with",a,"students will have",a//l,"groups")
# def sub(a,l=24):
    # sub=0
    # sub+=i%labgrp
    # sub+=b%labgrp
    # sub+=c%labgrp
    # print(sub//l)
for i in range(len(list)):
    main(list[i])
    # sub(list[i])

sub=0
sub+=list[0]%l
sub+=list[1]%l
sub+=list[2]%l
print("leftover group will have",sub,"students",)
# print("total groups needed: ",)
if sub>l:
    print("smaller leftover group will have",sub-l,"students")