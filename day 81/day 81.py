from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def check_robot():
    if request.method == 'POST':
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']

        # Define robot answers
        robot_answers = {
            'question1': 'yes',     
            'question2': '101010',  
            'question3': 'option3'  
        }

        if (question1 == robot_answers['question1'] or
            question2 == robot_answers['question2'] or
            question3 == robot_answers['question3']):
            return "You are a robot"
        else:
            return "You are human"
    
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Robot Check Form</title>
    </head>
    <body>
        <form method="POST">
            <label for="question1">Are you a made of metal? (yes or no)</label><br>
            <input type="radio" id="yes" name="question1" value="yes" required>
            <label for="yes">Yes</label><br>
            <input type="radio" id="no" name="question1" value="no" required>
            <label for="no">No</label><br><br>

            <label for="question2">What is infinity +1</label><br>
            <input type="text" id="question2" name="question2" required><br><br>

            <label for="question3">What is your favorite food?</label><br>
            <select id="question3" name="question3">
                <option value="option1">Human Food</option>
                <option value="option2">Synthetic Oil</option>
            </select><br><br>

            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
