# -*- coding: utf-8 -*- 

def ConnectToNexPort(self,  minimum):
    """사용 가능한 다음 포트에 연결한다. 새 minimum 포트를 반환한다."""
    if minimum <= 1024:
        raise ValueError('1025 이상의 포트를 입력해야 합니다.')
    port = self._FindNextOpenPort(minimum)
    if not port:
        raise ConnectionError('%d 포트에 연결할 수 없습니다. '% (minimum,))
    assert port >=minimum, '예상치 못한 %d 포트를 사용했습니다. 입력한 minimum 포트는 %d입니다. '%(port, minimum)
    return port

