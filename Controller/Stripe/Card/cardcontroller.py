import stripe

class CreditCard:
    async def crateCreditCard():
        stripe.api_key = "pk_test_51KJcErLcQbzaMHi3KJOMM6o37BnzcwfugGiug7CMwArPnZAj3sDjgC8hem7zK3QftcL5PrEWdGm4o4a8x1bRwjgA000KtljPp4"

        response=stripe.Token.create(
        card={
                "number": "4242424242424242",
                "exp_month": 1,
                "exp_year": 2023,
                "cvc": "314",
            },       
        )
        print(f'response {response}')
        return response

    async def paymentCard():
        token=await CreditCard.crateCreditCard()
        stripe.api_key='sk_test_51KJcErLcQbzaMHi3J36s4Udx2Be02PibkG1tPricmqRJ5pOzQemeQeJEXPNymvL8LBV1RBFtYReW0D6JfYi4FnCx00InWkfX5N'
        payment = stripe.Charge.create(
                    amount= int(100)*100,                  # convert amount to cents
                    currency='usd',
                    description='Example charge',
                    source=token['id'],
                    )
        print(payment)