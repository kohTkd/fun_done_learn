from expects import expect, equal, have_key
from mamba import description, context, it, before, shared_context, included_context

from app.controllers.sessions_controller import SessionsController
from app.entities.session import Session
from app.repositories.sessions_repository import SessionsRepository

from bin.dynamodb_migrator import DynamoDbMigrator


with description(SessionsController) as self:
    with before.all:
        self.migrator = DynamoDbMigrator('us-east-1')
        self.sessions_respository = SessionsRepository(region_name='us-east-1')

    with before.each:
        self.migrator.truncate_all()
        self.migrator.set_test_region()

    with description('create()'):
        with context('with valid parameters'):
            with before.each:
                self.title = 'Thit is a valid title'
                self.params = {'title': self.title}

            with it('returns Created response'):
                response = SessionsController.create(self.params)
                expect(response.status).to(equal(201))
                response_body = response.body
                expect(response_body['title']).to(equal(self.title))
                expect(response_body).to(have_key('token'))
                expect(response_body).to(have_key('created_at'))

            with it('saves session'):
                response_body = SessionsController.create(self.params).body
                token = response_body['token']
                created_at = response_body['created_at']
                session = self.sessions_respository.find(token)
                expect(session.token).to(equal(token))
                expect(str(session.created_at)).to(equal(created_at))

        with context('with invalid parameters'):
            with shared_context('Invalid parameters examples'):
                with before.each:
                    self.params = {'title': self.title}

                with it('returns Unprocessable Entity error'):
                    response = SessionsController.create(self.params)
                    expect(response.status).to(equal(422))
                    expect(response.body['errors']).to(equal(self.error_messages))

                with it('does not save session'):
                    SessionsController.create(self.params)
                    sessions = self.sessions_respository.scan()
                    expect(len(sessions)).to(equal(0))

            with context('with blank title'):
                with before.each:
                    self.title = ''
                    self.error_messages = ['タイトルは必須です']

                with included_context('Invalid parameters examples'):
                    pass

            with context('with too long title'):
                with before.each:
                    self.title = 'A' * 31
                    self.error_messages = ['タイトルは30文字以内で設定してください']

                with included_context('Invalid parameters examples'):
                    pass

    with description('show()'):
        with context('With exising token'):
            with before.each:
                self.token = 'SomeToken'
                self.session = Session(token=self.token, title='Some Title', persisted=True)
                self.sessions_respository.save(self.session)
                self.params = {'token': self.token}

            with it('returns OK response'):
                response = SessionsController.show(self.params)
                expect(response.status).to(equal(200))
                response_body = response.body
                expect(response_body['title']).to(equal('Some Title'))
                expect(response_body['token']).to(equal('SomeToken'))
                expect(response_body['created_at']).to(equal(str(self.session.created_at)))

        with context('With invalid token'):
            with before.each:
                self.params = {'token': 'InvalidToken'}

            with it('returns Not Fount error'):
                response = SessionsController.show(self.params)
                expect(response.status).to(equal(404))
                response_body = response.body
                expect(response.body['errors']).to(equal('セッションが見つかりません'))
