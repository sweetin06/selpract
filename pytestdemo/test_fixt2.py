import pytest

@pytest.mark.usefixtures("dataload")
class test2(Baseclass):
    def test_pro(self,dataload):
        log= self.getLogger
        log.info(dataload[0])
        log.info(dataload[2])
       # print(dataload[0])

        print(dataload[2])