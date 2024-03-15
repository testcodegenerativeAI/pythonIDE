from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to track completed programs
completed_programs = {
    'factorial': False,
    'sum_list': False,
    'reverse_string': False,
    'check_palindrome': False,
    'count_vowels': False
}

@app.route('/')
def dashboard():
    completed_count = sum(completed_programs.values())
    total_count = len(completed_programs)
    return render_template('dashboard.html', completed_programs=completed_programs, completed_count=completed_count, total_count=total_count)

@app.route('/questions?nbr=1', methods=['GET','POST'])
def palindrome():
    nbr=request.args.get('nbr')
    results = []
    user_code='''def check_palindrome(n):\n
                # Your code here'''
    ps='''Given a string n, check if it is palindrome or not.'''
    i =''' n = "abbabba" '''
    o = ''' 1 '''
    ex='''S is a palindrome'''
    if request.method == 'POST':
        user_code = request.form['code']
        user_namespace = {}
        exec(user_code, user_namespace)
        palindrome_function = user_namespace.get('check_palindrome')
        if palindrome_function:
            test_cases = [
                ("XEREX", 1),
                ("MADAM", 1),
                ("MAPLE", 0)
            ]
            all_passed = True

            for test_input, expected_output in test_cases:
                try:
                    user_output = palindrome_function(test_input)
                    if user_output == expected_output:
                        results.append((test_input, user_output, expected_output, "Passed"))
                    else:
                        results.append((test_input, user_output, expected_output, "Failed"))
                        all_passed = False
                except Exception as e:
                    results.append((test_input, None, expected_output, "Error"))
                    all_passed = False

            if all_passed:
                completed_programs['check_palindrome'] = True

    return render_template('questions.html',ps=ps,i=i,o=o,ex=ex,nbr=nbr,user_code=user_code, results=results, completed=completed_programs['check_palindrome'],heading='Check Palindrome')

@app.route('/questions?nbr=2', methods=['GET','POST'])
def vowels():
    nbr=request.args.get('nbr')
    results = []
    user_code='''def count_vowels(n):\n
                # Your code here'''
    ps='''For a given string n, find the number of vowels (a,e,i,o,u) present in the string'''
    i='''n="Oppenheimer"'''
    o='''5'''
    ex='''Number of occurances of vowels is 5'''
    if request.method == 'POST':
        user_code = request.form.get('code')
        print(user_code)
        user_namespace = {}
        exec(user_code, user_namespace)
        vowels_function = user_namespace.get('count_vowels')
        if vowels_function:
            test_cases = [
                ("gimme some time to think", 8),
                ("MADAM", 2),
                ("MAPLE", 2)
            ]
            all_passed = True

            for test_input, expected_output in test_cases:
                try:
                    user_output = vowels_function(test_input)
                    if user_output == expected_output:
                        results.append((test_input, user_output, expected_output, "Passed"))
                    else:
                        results.append((test_input, user_output, expected_output, "Failed"))
                        all_passed = False
                except Exception as e:
                    results.append((test_input, None, expected_output, "Error"))
                    all_passed = False

            if all_passed:
                completed_programs['count_vowels'] = True

    return render_template('questions.html',ps=ps,i=i,o=o,ex=ex,nbr=nbr, results=results, completed=completed_programs['count_vowels'],heading='Count Vowels',user_code=user_code)


@app.route('/questions?nbr=3', methods=['GET', 'POST'])
def factorial():
    nbr=request.args.get('nbr')
    results = []  # Initialize results as an empty list
    user_code='''def factorial(n):\n
                # Your code here'''
    ps='''For a given number n, find the factorial of that number.'''
    i='''n=6'''
    o='''720'''
    ex='''Factorial of 6 is 6!=6x5x4x3x2x1=720'''
    if request.method == 'POST':
        user_code = request.form['code']
        user_namespace = {}
        exec(user_code, user_namespace)
        factorial_function = user_namespace.get('factorial')
        
        if factorial_function:
            test_cases = [
                (5, 120),
                (0, 1),
                (1, 1),
                (4, 24)
            ]
            all_passed = True

            for test_input, expected_output in test_cases:
                try:
                    user_output = factorial_function(test_input)
                    if user_output == expected_output:
                        results.append((test_input, user_output, expected_output, "Passed"))
                    else:
                        results.append((test_input, user_output, expected_output, "Failed"))
                        all_passed = False
                except Exception as e:
                    results.append((test_input, None, expected_output, "Error"))
                    all_passed = False

            if all_passed:
                completed_programs['factorial'] = True

    return render_template('questions.html',ps=ps,i=i,o=o,ex=ex,nbr=nbr,user_code=user_code, results=results, completed=completed_programs['factorial'],heading='Find the Factorial')

@app.route('/questions?nbr=4', methods=['GET', 'POST'])
def sum_list():
    nbr=request.args.get('nbr')
    results = []  # Initialize results as an empty list
    user_code='''def list_sum(n):\n
                # Your code here'''
    ps='''For a given list n, find the sum of all the values present in the list.'''
    i='''n=[5,6,7,9,10,25]'''
    o='''62'''
    ex='''Sum of the values in the list is 52.'''
    if request.method == 'POST':
        user_code = request.form['code']
        user_namespace = {}
        exec(user_code, user_namespace)
        list_sum_function = user_namespace.get('list_sum')
        
        if list_sum_function:
            test_cases = [
                ([1, 2, 3], 6),
                ([4, 5, 6], 15),
                ([], 0)
            ]
            all_passed = True

            for test_input, expected_output in test_cases:
                try:
                    user_output = list_sum_function(test_input)
                    if user_output == expected_output:
                        results.append((test_input, user_output, expected_output, "Passed"))
                    else:
                        results.append((test_input, user_output, expected_output, "Failed"))
                        all_passed = False
                except Exception as e:
                    results.append((test_input, None, expected_output, "Error"))
                    all_passed = False

            if all_passed:
                completed_programs['sum_list'] = True

    return render_template('questions.html',ps=ps,i=i,o=o,ex=ex,nbr=nbr,user_code=user_code, results=results, completed=completed_programs['sum_list'],heading='Find sum of list')

@app.route('/questions?nbr=5', methods=['GET', 'POST'])
def reverse_string():
    nbr=request.args.get('nbr')
    results = []  # Initialize results as an empty list
    user_code='''def reverse_string(n):\n
                # Your code here'''
    ps='''For a given string n, reverse the string and return it.'''
    i='''n=Mexico'''
    o='''ocixeM'''
    ex='''Reversing the letters of Mexico gives ocixeM'''
    if request.method == 'POST':
        user_code = request.form['code']
        user_namespace = {}
        exec(user_code, user_namespace)
        reverse_string_function = user_namespace.get('reverse_string')
        
        if reverse_string_function:
            test_cases = [
                ("hello", "olleh"),
                ("python", "nohtyp"),
                ("", "")
            ]
            all_passed = True

            for test_input, expected_output in test_cases:
                try:
                    user_output = reverse_string_function(test_input)
                    if user_output == expected_output:
                        results.append((test_input, user_output, expected_output, "Passed"))
                    else:
                        results.append((test_input, user_output, expected_output, "Failed"))
                        all_passed = False
                except Exception as e:
                    results.append((test_input, None, expected_output, "Error"))
                    all_passed = False

            if all_passed:
                completed_programs['reverse_string'] = True

    return render_template('questions.html',nbr=nbr,user_code=user_code, results=results, completed=completed_programs['reverse_string'],heading='Reverse a string')

if __name__ == '__main__':
    app.run(debug=True)
