import  pytest

@pytest.mark.usefixtures("dataload")
class test2:
    def test_pro(self,dataload):
        print(dataload[0])
        print(dataload[2])