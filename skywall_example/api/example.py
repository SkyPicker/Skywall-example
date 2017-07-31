from aiohttp.web import json_response
from skywall.core.database import create_session
from skywall.core.signals import Signal
from skywall.core.api import register_api
from skywall_example.models.example import Example, before_example_create, after_example_create


before_get_example = Signal('before_get_example')
after_get_example = Signal('before_get_example')


@register_api('GET', '/example', before_get_example, after_get_example)
async def get_example(request):
    """
    ---
    tags:
      - Example module
    summary: Example API
    description: Example Skywall module API endpoint
    produces:
      - application/json
    responses:
      200:
        description: Example response
        schema:
          type: object
          title: GetExample
          required:
            - message
          properties:
            message:
              type: string
    """
    with create_session() as session:
        example = Example(value='Example value')
        before_example_create.emit(session=session, example=example)
        session.add(example)
        session.flush()
        after_example_create.emit(session=session, example=example)
        return json_response({'message': 'Example response'})
