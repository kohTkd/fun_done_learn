from expects import expect, equal, have_key
from mamba import description, context, it, before

from app.controllers.sessions.activities.placement_controller import PlacementController
from app.entities.session import Session
from app.entities.activity import Activity
from app.entities.placement import Placement
from app.repositories.sessions_repository import SessionsRepository
from app.repositories.activities_repository import ActivitiesRepository
from app.repositories.placements_repository import PlacementsRepository

from bin.migrate import DynamoDbMigrator


with description(PlacementController) as self:
    with before.all:
        self.migrator = DynamoDbMigrator('us-east-1')
        self.sessions_respository = SessionsRepository(region_name='us-east-1')
        self.activities_repository = ActivitiesRepository(region_name='us-east-1')
        self.placements_repository = PlacementsRepository(region_name='us-east-1')

    with before.each:
        self.migrator.truncate_all()
        self.migrator.set_test_region()

    with description('upsert()'):
        with context('when specified session is present'):
            with before.each:
                self.session = Session(token='SessionToken', title='Some Title')
                self.sessions_respository.save(self.session)

            with context('when specified activity is present'):
                with before.each:
                    self.activity = Activity(session_token=self.session.token, token='ActivityToken', content='Content')
                    self.activities_repository.save(self.activity)

                with context('when placement is already present'):
                    with before.each:
                        self.placement = Placement(
                            session_token=self.session.token, activity_token=self.activity.token, left=10, top=20
                        )
                        self.placements_repository.save(self.placement)

                    with context('with valid parameters'):
                        with before.each:
                            self.params = {
                                'session_token': self.session.token, 'activity_token': self.activity.token,
                                'left': 100, 'top': 200
                            }

                        with it('returns OK response'):
                            response = PlacementController.upsert(self.params)
                            expect(response.status).to(equal(200))
                            response_body = response.body
                            expect(response_body['session_token']).to(equal(self.session.token))
                            expect(response_body['activity_token']).to(equal(self.activity.token))
                            expect(response_body).to(have_key('left'))
                            expect(response_body).to(have_key('top'))
                            expect(response_body).to(have_key('created_at'))
                            expect(response_body).to(have_key('updated_at'))

                        with it('updates placement'):
                            PlacementController.upsert(self.params)
                            placement = self.placements_repository.find(self.session.token, self.activity.token)
                            expect(placement.left).to(equal(100))
                            expect(placement.top).to(equal(200))
                            expect(placement.created_at).to(equal(self.placement.created_at))
                            expect(placement.updated_at).not_to(equal(self.placement.updated_at))

                    with context('with invalid parameters'):
                        with before.each:
                            self.params = {
                                'session_token': self.session.token, 'activity_token': self.activity.token,
                                'left': -100, 'top': 200
                            }

                        with it('returns Unprocessable Entity error'):
                            response = PlacementController.upsert(self.params)
                            expect(response.status).to(equal(422))
                            expect(response.body['errors']).to(equal(['左からの座標は0以上で設定してください']))

                        with it('does not update placement'):
                            PlacementController.upsert(self.params)
                            placement = self.placements_repository.find(self.session.token, self.activity.token)
                            expect(placement.left).to(equal(10))
                            expect(placement.top).to(equal(20))
                            expect(placement.created_at).to(equal(self.placement.created_at))
                            expect(placement.updated_at).to(equal(self.placement.updated_at))

                with context('when placement is absent'):
                    with context('with valid parameters'):
                        with before.each:
                            self.params = {
                                'session_token': self.session.token, 'activity_token': self.activity.token,
                                'left': 100, 'top': 200
                            }

                        with it('returns OK response'):
                            response = PlacementController.upsert(self.params)
                            expect(response.status).to(equal(200))
                            response_body = response.body
                            expect(response_body['session_token']).to(equal(self.session.token))
                            expect(response_body['activity_token']).to(equal(self.activity.token))
                            expect(response_body).to(have_key('left'))
                            expect(response_body).to(have_key('top'))
                            expect(response_body).to(have_key('created_at'))
                            expect(response_body).to(have_key('updated_at'))

                        with it('creates placement'):
                            PlacementController.upsert(self.params)
                            placement = self.placements_repository.find(self.session.token, self.activity.token)
                            expect(placement.left).to(equal(100))
                            expect(placement.top).to(equal(200))

                    with context('with invalid parameters'):
                        with before.each:
                            self.params = {
                                'session_token': self.session.token, 'activity_token': self.activity.token,
                                'left': -100, 'top': 200
                            }

                        with it('returns Unprocessable Entity error'):
                            response = PlacementController.upsert(self.params)
                            expect(response.status).to(equal(422))
                            expect(response.body['errors']).to(equal(['左からの座標は0以上で設定してください']))

                        with it('does not create placement'):
                            PlacementController.upsert(self.params)
                            placements = self.placements_repository.scan()
                            expect(len(placements)).to(equal(0))

            with context('when specified activity is absent'):
                with before.each:
                    self.params = {
                        'session_token': self.session.token, 'activity_token': 'InvalidToken',
                        'left': 100, 'top': 200
                    }

                with it('returns Not Found response'):
                    response = PlacementController.upsert(self.params)
                    expect(response.status).to(equal(404))
                    response_body = response.body
                    expect(response.body['errors']).to(equal('アクティビティが見つかりません'))

        with context('when specified session is absent'):
            with before.each:
                self.params = {
                    'session_token': 'InvalidToken', 'activity_token': 'InvalidToken', 'left': 100, 'top': 200
                }

            with it('returns Not Found response'):
                response = PlacementController.upsert(self.params)
                expect(response.status).to(equal(404))
                response_body = response.body
                expect(response.body['errors']).to(equal('セッションが見つかりません'))
