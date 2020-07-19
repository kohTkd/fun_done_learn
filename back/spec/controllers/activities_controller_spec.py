from expects import expect, equal, have_key
from mamba import description, context, it, before, shared_context, included_context

from app.controllers.sessions.activities_controller import ActivitiesController
from app.entities.session import Session
from app.entities.activity import Activity
from app.repositories.sessions_repository import SessionsRepository
from app.repositories.activities_repository import ActivitiesRepository

from bin.dynamodb_migrator import DynamoDbMigrator


with description(ActivitiesController) as self:
    with before.all:
        self.migrator = DynamoDbMigrator('us-east-1')
        self.sessions_respository = SessionsRepository(region_name='us-east-1')
        self.activities_repository = ActivitiesRepository(region_name='us-east-1')

    with before.each:
        self.migrator.truncate_all()
        self.migrator.set_test_region()

    with description('create()'):
        with context('when specified session is present'):
            with before.each:
                self.session_token = 'SomeToken'
                self.session = Session(token=self.session_token, title='Some Title')
                self.sessions_respository.save(self.session)

            with context('with valid parameters'):
                with before.each:
                    self.content = 'This is a valid Content'
                    self.params = {'content': self.content, 'session_token': self.session_token}

                with it('returns Created response'):
                    response = ActivitiesController.create(self.params)
                    expect(response.status).to(equal(201))
                    response_body = response.body
                    expect(response_body['content']).to(equal(self.content))
                    expect(response_body['session_token']).to(equal(self.session_token))
                    expect(response_body).to(have_key('token'))
                    expect(response_body).to(have_key('created_at'))
                    expect(response_body).to(have_key('updated_at'))

                with it('saves activity'):
                    response_body = ActivitiesController.create(self.params).body
                    token = response_body['token']
                    created_at = response_body['created_at']
                    updated_at = response_body['updated_at']
                    activity = self.activities_repository.find(self.session_token, token)
                    expect(activity.token).to(equal(token))
                    expect(str(activity.created_at)).to(equal(created_at))
                    expect(str(activity.updated_at)).to(equal(updated_at))

            with context('with invalid parameters'):
                with shared_context('Invalid parameters examples'):
                    with before.each:
                        self.params = {'content': self.content, 'session_token': self.session_token}

                    with it('returns Unprocessable Entity error'):
                        response = ActivitiesController.create(self.params)
                        expect(response.status).to(equal(422))
                        expect(response.body['errors']).to(equal(self.error_messages))

                    with it('does not save activity'):
                        ActivitiesController.create(self.params)
                        activities = self.activities_repository.scan()
                        expect(len(activities)).to(equal(0))

                with context('with blank content'):
                    with before.each:
                        self.content = ''
                        self.error_messages = ['内容は必須です']

                    with included_context('Invalid parameters examples'):
                        pass

                with context('with too long title'):
                    with before.each:
                        self.content = 'A' * 101
                        self.error_messages = ['内容は100文字以内で設定してください']

                    with included_context('Invalid parameters examples'):
                        pass

        with context('when specified session is absent'):
            with before.each:
                self.session_token = 'SomeToken'
                self.content = 'This is a valid Content'
                self.params = {'content': self.content, 'session_token': self.session_token}

            with it('returns Not Found response'):
                response = ActivitiesController.create(self.params)
                expect(response.status).to(equal(404))
                response_body = response.body
                expect(response.body['errors']).to(equal('セッションが見つかりません'))

    with description('index()'):
        with context('when specified session is present'):
            with shared_context('Valid session examples'):
                with it('returns OK response'):
                    response = ActivitiesController.index(self.params)
                    expect(response.status).to(equal(200))
                    for response_note, activity in zip(response.body, self.activities):
                        expect(response_note['session_token']).to(equal(activity.session_token))
                        expect(response_note['token']).to(equal(activity.token))
                        expect(response_note['content']).to(equal(activity.content))
                        expect(response_note['created_at']).to(equal(str(activity.created_at)))
                        expect(response_note['updated_at']).to(equal(str(activity.updated_at)))

            with before.each:
                self.session_token = 'SomeToken'
                self.session = Session(token=self.session_token, title='Some Title')
                self.sessions_respository.save(self.session)

                self.params = {'session_token': self.session_token}

            with context('when sticky notes are present'):
                with before.each:
                    self.activities = [
                        Activity(session_token=self.session.token, token='token1', content='Content1'),
                        Activity(session_token=self.session.token, token='token2', content='Content2')
                    ]
                    self.activities_repository.save(self.activities)

                with included_context('Valid session examples'):
                    pass

                with context('when other session is present'):
                    with before.each:
                        self.other_note = Activity(session_token='OtherToken', token='token', content='Content')
                        self.activities_repository.save(self.other_note)

                    with it('not returns other session activity'):
                        response = ActivitiesController.index(self.params)
                        expect(any([note['token'] == self.other_note.token for note in response.body])).to(equal(False))

            with context('when sticky notes are absent'):
                with before.each:
                    self.activities = []

                with included_context('Valid session examples'):
                    pass

        with context('when specified session is absent'):
            with before.each:
                self.session_token = 'SomeToken'
                self.params = {'session_token': self.session_token}

            with it('returns Not Found response'):
                response = ActivitiesController.index(self.params)
                expect(response.status).to(equal(404))
                response_body = response.body
                expect(response.body['errors']).to(equal('セッションが見つかりません'))
