import stripe

class bankController:

    async def createBankToken():
            stripe.api_key = "pk_test_51KJcErLcQbzaMHi3KJOMM6o37BnzcwfugGiug7CMwArPnZAj3sDjgC8hem7zK3QftcL5PrEWdGm4o4a8x1bRwjgA000KtljPp4"

            response=stripe.Token.create(
            bank_account={
                    "number": "4242424242424242",
                    "exp_month": 1,
                    "exp_year": 2023,
                    "cvc": "314",
                },       
            )
            print(f'response {response}')
            return response