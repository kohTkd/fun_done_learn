from expects import expect, equal, have_key
from mamba import description, context, it, before, shared_context, included_context

from app.controllers.sessions.activities_controller import ActivitiesController
from app.entities.session import Session
from app.entities.activity import Activity
from app.repositories.sessions_repository import SessionsRepository
from app.repositories.activities_repository import ActivitiesRepository
from app.repositories.placements_repository import PlacementsRepository

from bin.migrate import DynamoDbMigrator


with description(ActivitiesController) as self:
    with before.all:
        self.migrator = DynamoDbMigrator('us-east-1')
        self.sessions_respository = SessionsRepository(region_name='us-east-1')
        self.activities_repository = ActivitiesRepository(region_name='us-east-1')
        self.placements_repository = PlacementsRepository(region_name='us-east-1')

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
                    response_placement = response.body.get('placement')
                    expect(response_placement['left']).to(equal(0))
                    expect(response_placement['top']).to(equal(0))

                with it('saves activity'):
                    response_body = ActivitiesController.create(self.params).body
                    token = response_body['token']
                    activity = self.activities_repository.find(self.session_token, token)
                    expect(activity.content).to(equal(self.content))

                with it('creates placement'):
                    response_body = ActivitiesController.create(self.params).body
                    token = response_body['token']
                    placement = self.placements_repository.find(self.session_token, token)
                    expect(placement.left).to(equal(0))
                    expect(placement.top).to(equal(0))

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

                    with it('does not create placement'):
                        ActivitiesController.create(self.params)
                        placements = self.placements_repository.scan()
                        expect(len(placements)).to(equal(0))

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
                    for response_activity, activity in zip(response.body, self.activities):
                        expect(response_activity['session_token']).to(equal(activity.session_token))
                        expect(response_activity['token']).to(equal(activity.token))
                        expect(response_activity['content']).to(equal(activity.content))
                        expect(response_activity['created_at']).to(equal(str(activity.created_at)))
                        expect(response_activity['updated_at']).to(equal(str(activity.updated_at)))

                        placement = activity.placement
                        response_placement = response_activity['placement']
                        expect(response_placement['session_token']).to(equal(placement.session_token))
                        expect(response_placement['activity_token']).to(equal(placement.activity_token))
                        expect(int(response_placement['left'])).to(equal(placement.left))
                        expect(int(response_placement['top'])).to(equal(placement.top))
                        expect(response_placement['created_at']).to(equal(str(placement.created_at)))
                        expect(response_placement['updated_at']).to(equal(str(placement.updated_at)))

            with before.each:
                self.session_token = 'SomeToken'
                self.session = Session(token=self.session_token, title='Some Title')
                self.sessions_respository.save(self.session)

                self.params = {'session_token': self.session_token}

            with context('when activities are present'):
                with before.each:
                    self.activities = [
                        Activity(session_token=self.session.token, token='token1', content='Content1'),
                        Activity(session_token=self.session.token, token='token2', content='Content2')
                    ]
                    self.activities_repository.save(self.activities)

                with context('when placements are present'):
                    with before.each:
                        self.placements = [activity.placement for activity in self.activities]
                        for placement, i in zip(self.placements, range(2)):
                            placement.left = i * 10 + 1
                            placement.top = i * 20 + 1
                        self.placements_repository.save(self.placements)

                    with included_context('Valid session examples'):
                        pass

                with context('when placements are absent'):
                    with before.each:
                        self.placements = [activity.placement for activity in self.activities]
                        for placement in self.placements:
                            placement.left = 0
                            placement.top = 0

                    with included_context('Valid session examples'):
                        pass

                with context('when other session is present'):
                    with before.each:
                        self.other_note = Activity(session_token='OtherToken', token='token', content='Content')
                        self.activities_repository.save(self.other_note)

                    with it('not returns other session activity'):
                        response = ActivitiesController.index(self.params)
                        expect(any([note['token'] == self.other_note.token for note in response.body])).to(equal(False))

            with context('when activities are absent'):
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

    with description('update()'):
        with context('when specified session is present'):
            with before.each:
                self.session_token = 'SomeToken'
                self.session = Session(token=self.session_token, title='Some Title')
                self.sessions_respository.save(self.session)

            with context('when specified activity is present'):
                with before.each:
                    self.token = 'ActivityToken'
                    self.activity = Activity(session_token=self.session.token, token=self.token, content='Content')
                    self.activities_repository.save(self.activity)

                with context('with valid parameters'):
                    with before.each:
                        self.content = 'This is a valid Content'
                        self.params = {
                            'content': self.content, 'session_token': self.session_token, 'token': self.token
                        }

                    with it('returns OK response'):
                        response = ActivitiesController.update(self.params)
                        expect(response.status).to(equal(200))
                        response_body = response.body
                        expect(response_body['content']).to(equal(self.content))
                        expect(response_body['session_token']).to(equal(self.session_token))
                        expect(response_body['token']).to(equal(self.token))
                        expect(response_body['content']).to(equal(self.content))
                        expect(response_body).to(have_key('created_at'))
                        expect(response_body).to(have_key('updated_at'))

                    with it('updates activity'):
                        ActivitiesController.update(self.params).body
                        activity = self.activities_repository.find(self.session_token, self.token)
                        expect(activity.content).to(equal(self.content))
                        expect(activity.updated_at).not_to(equal(self.activity.updated_at))

                with context('with invalid parameters'):
                    with shared_context('Invalid parameters examples'):
                        with before.each:
                            self.params = {
                                'content': self.content, 'session_token': self.session_token, 'token': self.token
                            }

                        with it('returns Unprocessable Entity error'):
                            response = ActivitiesController.update(self.params)
                            expect(response.status).to(equal(422))
                            expect(response.body['errors']).to(equal(self.error_messages))

                        with it('does not update activity'):
                            ActivitiesController.update(self.params)
                            activity = self.activities_repository.find(self.session_token, self.token)
                            expect(activity.content).to(equal(self.activity.content))
                            expect(activity.updated_at).to(equal(self.activity.updated_at))

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

            with context('when specified activity is absent'):
                with before.each:
                    self.params = {'content': 'Content', 'session_token': self.session.token, 'token': 'InvalidToken'}

                with it('returns Not Found response'):
                    response = ActivitiesController.update(self.params)
                    expect(response.status).to(equal(404))
                    response_body = response.body
                    expect(response.body['errors']).to(equal('アクティビティが見つかりません'))

        with context('when specified session is absent'):
            with before.each:
                self.session_token = 'SomeToken'
                self.content = 'This is a valid Content'
                self.params = {'content': self.content, 'session_token': self.session_token}

            with it('returns Not Found response'):
                response = ActivitiesController.update(self.params)
                expect(response.status).to(equal(404))
                response_body = response.body
                expect(response.body['errors']).to(equal('セッションが見つかりません'))
