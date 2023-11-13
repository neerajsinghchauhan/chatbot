from flask import Flask ,render_template, request, jsonify
import openai 
import time

app = Flask(__name__)

openai.api_key = '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'

conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response' , methods = ['POST'])
def get_response():
    user_input = request.form['user_input']

    if user_input.lower() == 'exit':
        return jsonify({'response': 'Goodbye!'})

    update_message(user_input)
    response = get_api_response(user_input)

#set a simulate delay
    time.sleep(2)

    return jsonify({'response': response})

def get_api_response(prompt):
    text = None
    try:
        conversation = '\n'.join(conversation_history + [f'You: {prompt}'])
        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = conversation,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6
        )

        text = response['choices'][0]['text']

    except Exception as e:
        print('Error:',e)

    return text

def update_message(message):
    conversation_history.append(f'User: {message}')


if __name__ == '__main__':
    app.run(debug=True)            
        







