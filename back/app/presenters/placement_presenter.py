class PlacementPresenter():
    def __init__(self, placement):
        self.placement = placement

    def detail(self) -> dict:
        return {
            'session_token': self.placement.session_token,
            'activity_token': self.placement.activity_token,
            'left': int(self.placement.left),
            'top': int(self.placement.top),
            'created_at': str(self.placement.created_at),
            'updated_at': str(self.placement.updated_at)
        }
