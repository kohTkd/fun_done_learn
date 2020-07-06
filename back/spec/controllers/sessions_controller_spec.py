from expects import expect, equal, have_key
from mamba import description, context, it, before

from app.controllers.sessions_controller import SessionsController
from app.repositories.sessions_repository import SessionsRepository

from bin.dynamodb_migrator import DynamoDbMigrator

with description(SessionsController) as self:
    with before.all:
        self.migrator = DynamoDbMigrator('us-east-1')
        self.migrator.set_test_region()

    with before.each:
        self.migrator.truncate_all()

    with description('create()'):
        with context('with valid parameters'):
            with before.each:
                self.title = 'Thit is a valid title'
                self.params = {'title': self.title}

            with it('returns status 201'):
                response = SessionsController.create(self.params)
                expect(response.status).to(equal(201))

            with it('returns created resource'):
                response_body = SessionsController.create(self.params).body
                expect(response_body['title']).to(equal(self.title))
                expect(response_body).to(have_key('token'))
                expect(response_body).to(have_key('created_at'))

            with it('save session'):
                response_body = SessionsController.create(self.params).body
                token = response_body['token']
                created_at = response_body['created_at']
                session = SessionsRepository().find(token)
                expect(session.token).to(equal(token))
                expect(str(session.created_at)).to(equal(created_at))
