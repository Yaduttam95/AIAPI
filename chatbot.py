import pprint
import google.generativeai as palm

my_key = 'AIzaSyDBpKKyAlprgXQi3L1VxQXzoZzyu6i7wek'

palm.configure(api_key=my_key)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
#print(model)

prompt_user = input("Enter Subject of Email: ")

completion = palm.generate_text(
    model=model,
    prompt=prompt_user,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)