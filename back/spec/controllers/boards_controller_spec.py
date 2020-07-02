from expects import expect, equal, have_key
from mamba import description, context, it, before

from app.controllers.boards_controller import BoardsController
from app.repositories.boards_repository import BoardsRepository

from bin.dynamodb_migrator import DynamoDbMigrator

with description(BoardsController) as self:
    with before.all:
        self.migrator = DynamoDbMigrator('us-east-1')

    with before.each:
        self.migrator.truncate_all()

    with description('create()'):
        with context('with valid parameters'):
            with before.each:
                self.title = 'Thit is a valid title'
                self.params = {'title': self.title}

            with it('returns status 201'):
                response = BoardsController.create(self.params)
                expect(response.status).to(equal(201))

            with it('returns created resource'):
                response_body = BoardsController.create(self.params).body
                expect(response_body['title']).to(equal(self.title))
                expect(response_body).to(have_key('token'))
                expect(response_body).to(have_key('created_at'))

            with it('save board'):
                response_body = BoardsController.create(self.params).body
                token = response_body['token']
                created_at = response_body['created_at']
                board = BoardsRepository().find(token)
                expect(board.token).to(equal(token))
                expect(str(board.created_at)).to(equal(created_at))
