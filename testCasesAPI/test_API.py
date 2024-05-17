import pytest, json

from common.api_common_methods import APICommonMethods

class Test_API:

    Endpoint_MoviesList = "/api/films"
    MovieCount = 6
    ThirdMovieDirector = "Richard Marquand"
    FifthMovieProducers = ("Gary Kurtz", "George Lucas")

    def setup_class(self):
        self.apiMethods = APICommonMethods()

    @pytest.mark.api
    def test_CheckMovieCount(self):
        response = self.apiMethods.api_get(self.Endpoint_MoviesList)
        item_dict = json.loads(json.dumps(response))
        print(len(item_dict['results']))
        assert len(item_dict['results']) == self.MovieCount

    @pytest.mark.api
    def test_CheckThirdMovieDirector(self):
        response = self.apiMethods.api_get(self.Endpoint_MoviesList)
        item_dict = json.loads(json.dumps(response))
        print(item_dict['results'][2]['director'])
        assert item_dict['results'][2]['director'] == self.ThirdMovieDirector

    @pytest.mark.api
    def test_AssertFifthMovieProducers(self):
        response = self.apiMethods.api_get(self.Endpoint_MoviesList)
        item_dict = json.loads(json.dumps(response))
        print(item_dict['results'][5]['producer'])
        assert item_dict['results'][5]['producer'] not in self.FifthMovieProducers
