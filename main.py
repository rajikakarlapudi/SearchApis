from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your existing API endpoint
EXISTING_API_URL = "https://app.ylytic.com/ylytic/test"

def search_comments(search_params):
    response = requests.get(EXISTING_API_URL, params=search_params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
@app.route('/search_comments', methods=['GET'])
def search_comments_api():
    search_params = {}

    search_author = request.args.get('search_author')
    if search_author:
        search_params['author'] = search_author

    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    if at_from and at_to:
        search_params['at_from'] = at_from
        search_params['at_to'] = at_to

    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    if like_from and like_to:
        search_params['like_from'] = like_from
        search_params['like_to'] = like_to

    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    if reply_from and reply_to:
        search_params['reply_from'] = reply_from
        search_params['reply_to'] = reply_to

    search_text = request.args.get('search_text')
    if search_text:
        search_params['search_text'] = search_text

    result = search_comments(search_params)
    if result is not None:
        return jsonify(result)
    else:
        return jsonify({'error': 'An error occurred while fetching comments.'}), 500

if __name__ == '__main__':
    app.run()
