def Basket(self,price):
    self.price=price
    sum=0
    for i in range(price):
        if price[i]>=500:
            discount(price)
        else:
            sum = discount()+sum.append(price)
    return sum
def discount(dis):
    for i in GST:
        for j in sum:
            for k in quantity:
                discount=sum[j]*((GST [i]-dis)/100)*quantity[k]
    return discount
# products = ["leather wallet", "umbrella", "cigarette", "honey"]
price = [1100, 900, 200, 100]
GST = [18, 12, 28, 0]
quantity = [1, 4, 3, 2]
x=Basket(1,500)
y=discount(5)
print(x)
print(y)