from expects import expect, equal, have_key
from mamba import description, context, it, before, shared_context, included_context

from app.controllers.sessions.notes_controller import NotesController
from app.entities.session import Session
from app.entities.note import Note
from app.repositories.sessions_repository import SessionsRepository
from app.repositories.notes_repository import NotesRepository

from bin.migrate import DynamoDbMigrator


with description(NotesController) as self:
    with before.all:
        self.migrator = DynamoDbMigrator('us-east-1')
        self.sessions_respository = SessionsRepository(region_name='us-east-1')
        self.notes_repository = NotesRepository(region_name='us-east-1')

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
                    response = NotesController.create(self.params)
                    expect(response.status).to(equal(201))
                    response_body = response.body
                    expect(response_body['content']).to(equal(self.content))
                    expect(response_body['session_token']).to(equal(self.session_token))
                    expect(response_body).to(have_key('token'))
                    expect(response_body).to(have_key('created_at'))
                    expect(response_body).to(have_key('updated_at'))

                with it('saves note'):
                    response_body = NotesController.create(self.params).body
                    token = response_body['token']
                    note = self.notes_repository.find(self.session_token, token)
                    expect(note.content).to(equal(self.content))

            with context('with invalid parameters'):
                with shared_context('Invalid parameters examples'):
                    with before.each:
                        self.params = {'content': self.content, 'session_token': self.session_token}

                    with it('returns Unprocessable Entity error'):
                        response = NotesController.create(self.params)
                        expect(response.status).to(equal(422))
                        expect(response.body['errors']).to(equal(self.error_messages))

                    with it('does not save note'):
                        NotesController.create(self.params)
                        notes = self.notes_repository.scan()
                        expect(len(notes)).to(equal(0))

                with context('with blank content'):
                    with before.each:
                        self.content = ''
                        self.error_messages = ['内容は必須です']

                    with included_context('Invalid parameters examples'):
                        pass

                with context('with too long title'):
                    with before.each:
                        self.content = 'A' * 201
                        self.error_messages = ['内容は200文字以内で設定してください']

                    with included_context('Invalid parameters examples'):
                        pass

        with context('when specified session is absent'):
            with before.each:
                self.session_token = 'SomeToken'
                self.content = 'This is a valid Content'
                self.params = {'content': self.content, 'session_token': self.session_token}

            with it('returns Not Found response'):
                response = NotesController.create(self.params)
                expect(response.status).to(equal(404))
                response_body = response.body
                expect(response.body['errors']).to(equal('セッションが見つかりません'))

    with description('index()'):
        with context('when specified session is present'):
            with shared_context('Valid session examples'):
                with it('returns OK response'):
                    response = NotesController.index(self.params)
                    expect(response.status).to(equal(200))
                    for response_note, note in zip(response.body, self.notes):
                        expect(response_note['session_token']).to(equal(note.session_token))
                        expect(response_note['content']).to(equal(note.content))
                        expect(response_note['created_at']).to(equal(str(note.created_at)))
                        expect(response_note['updated_at']).to(equal(str(note.updated_at)))

            with before.each:
                self.session_token = 'SomeToken'
                self.session = Session(token=self.session_token, title='Some Title')
                self.sessions_respository.save(self.session)

                self.params = {'session_token': self.session_token}

            with context('when notes are present'):
                with before.each:
                    self.notes = [
                        Note(session_token=self.session.token, token='token1', content='Content1'),
                        Note(session_token=self.session.token, token='token2', content='Content2')
                    ]
                    self.notes_repository.save(self.notes)

                with included_context('Valid session examples'):
                    pass

                with context('when other session is present'):
                    with before.each:
                        self.other_note = Note(session_token='OtherToken', token='token', content='Content')
                        self.notes_repository.save(self.other_note)

                    with it('not returns other session note'):
                        response = NotesController.index(self.params)
                        expect(
                            any([note['token'] == self.other_note.token for note in response.body])
                        ).to(equal(False))

            with context('when notes are absent'):
                with before.each:
                    self.notes = []

                with included_context('Valid session examples'):
                    pass

        with context('when specified session is absent'):
            with before.each:
                self.session_token = 'SomeToken'
                self.params = {'session_token': self.session_token}

            with it('returns Not Found response'):
                response = NotesController.index(self.params)
                expect(response.status).to(equal(404))
                response_body = response.body
                expect(response.body['errors']).to(equal('セッションが見つかりません'))
