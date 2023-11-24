from flask import Flask, request, jsonify
import google.generativeai as palm
import pprint

app = Flask(__name__)

# Configure your API key and model
my_key = 'AIzaSyDBpKKyAlprgXQi3L1VxQXzoZzyu6i7wek'  # Replace with your actual API key
palm.configure(api_key=my_key)
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

@app.route('/generate_text', methods=['POST'])
def generate_text():
    data = request.get_json()
    prompt_user = data.get('input_string', '')  # Get the input string from the request

    completion = palm.generate_text(
        model=model,
        prompt=prompt_user,
        temperature=0,
        max_output_tokens=800,
    )

    response = {'output_string': completion.result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
