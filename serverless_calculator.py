import json

def check_params(body):
    for key, value in body.items():
        if key == 'a' or key == 'b':
            if type(int(value)) != int:
                return {'statusCode':400,'body':json.dumps(f'value of {key} is not number')}
        if key == 'op':
            if value not in '+-*/':
                return {'statusCode':400,'body':json.dumps(f'value of {key} is not operands')}
        if key == '':
            return {'statusCode':400,'body':json.dumps(f'key cannot be empty string')}
        if key not in 'abop':
            return {'statusCode':400,'body':json.dumps(f'wrong param name {key} not a, b or op')}
        
def lambda_operation(body):
    a = int(body['a'])
    b = int(body['b'])
    op = body['op']
    ans = 0
    if op == '+':
        ans = a + b
    if op == '-':
        ans = a - b
    if op == '*':
        ans = a * b
    if op == '/':
        ans = a / b
    return ans

def lambda_handler(event, context):

    eventString = json.dumps(event)
    eventDict = json.loads(eventString)
    body = eventDict['body']
    check_params(body)
    response = dict()
    response['result'] = lambda_operation(body)

    return {
    'statusCode': 200,
    'body': json.dumps(response)
    }
