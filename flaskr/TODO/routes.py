from flask import Blueprint, jsonify, request, abort
from flaskr.models.models import Todo


todo = Blueprint('todo', __name__)


@todo.route('/api/todos')
def get_todos():
    todos = Todo.query.order_by('id').all()

    if not todos:
        abort(404)

    todos = [t.display() for t in todos]

    return jsonify({
        'page': 'Todos-List',
        'body': todos,
        "success": True
    })


@todo.route('/api/todos/<int:todo_id>')
def get_todo(todo_id):
    todo_ = Todo.query.get(todo_id)

    if not todo_:
        abort(404)

    todo_ = todo_.display()

    return jsonify({
        'page': f'Todo #{todo_id}',
        'body': todo_,
        'success': True
    })


@todo.route('/api/todos', methods=['POST'])
def create_todos():
    body = request.get_json()

    content = body.get('content')
    finished = False

    if not content:
        abort(400)

    new_todo = Todo(content=content, finished=finished)

    try:
        new_todo.insert()
    except Exception as e:
        print(e)
        abort(422)

    todos = [t.display() for t in Todo.query.order_by('id').all()]

    return jsonify({
        'page': 'Todos-List',
        'body': todos,
        'success': True
    })


@todo.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    todo_ = Todo.query.get(todo_id)

    if not todo_:
        abort(404)

    try:
        todo_.delete()
    except Exception as e:
        print(e)
        abort(422)

    return jsonify({
        'page': 'Todos-List',
        'body': f'Todo #{todo_id} Deleted',
        'success': True
    })


@todo.route('/api/todos/<int:todo_id>', methods=['PATCH'])
def update_todos(todo_id):
    todo_ = Todo.query.get(todo_id)

    if not todo_:
        abort(404)

    body = request.get_json()

    if not body:
        abort(400)

    finished = body.get('finished')

    try:
        todo_.finished = finished
        todo_.update()
    except Exception as e:
        print(e)
        abort(422)

    todos = [t.display() for t in Todo.query.order_by('id').all()]

    return jsonify({
        'page': 'Todos-List',
        'body': todos,
        'success': True
    })
